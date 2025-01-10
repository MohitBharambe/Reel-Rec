import aiohttp
import asyncio
import diskcache as dc
import os
from dotenv import load_dotenv
import random as rd
import joblib
from .forms import top_movies_df  # top movies dataframe

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
# Caching the API responses
cache = dc.Cache(os.path.join(os.path.dirname(__file__), '..', 'reel_rec-cache'))

# Load the model data
movies = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'Model/movies_list.joblib'))
similarity = joblib.load(os.path.join(os.path.dirname(__file__), '..', 'Model/similars_list.joblib'))


#  Fetch Poster
async def fetch_poster(session, id, semaphore):
    if id in cache:
        cached_data = cache[id]
        if isinstance(cached_data, dict):
            return id, cached_data.get('poster_url'), cached_data.get('backdrop_url')
        else:
            return id, None, None
    
    url = f"https://api.themoviedb.org/3/movie/{id}/images?include_image_language=en"
    async with semaphore:
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                poster_url = None
                backdrop_url = None

                poster_list = data.get("posters", [])
                for poster in poster_list:
                    width = poster.get("width")
                    height = poster.get("height")
                    if width <= 2000 and height > width:
                        file_path = poster.get("file_path")
                        poster_url = f"https://image.tmdb.org/t/p/w780{file_path}"
                        break

                backdrop_list = data.get("backdrops", [])
                for backdrop in backdrop_list:
                    width = backdrop.get("width")
                    height = backdrop.get("height")
                    if width <= 3840 and height < width:
                        file_path = backdrop.get("file_path")
                        backdrop_url = f"https://image.tmdb.org/t/p/w780{file_path}"
                        break

                if poster_url or backdrop_url:
                    cache[id] = {"poster_url": poster_url, "backdrop_url": backdrop_url}
                    return id, poster_url, backdrop_url
        except aiohttp.ClientError as e:
            return(f"Error fetching poster for ID {id}: {e}")
        except Exception as e:
            return(f"An unexpected error occurred for ID {id}: {e}")
    return id, None, None

# Fetch Multiple Posters & Backdrops
async def fetch_posters(ids):
    posters = {}
    backdrops = {}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('bearer_token')}"
    }
    
    semaphore = asyncio.Semaphore(40) 
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [fetch_poster(session, id, semaphore) for id in ids]
        results = await asyncio.gather(*tasks)
        for id, poster_url, backdrop_url in results:
            if poster_url:
                posters[id] = poster_url
            if backdrop_url:
                backdrops[id] = backdrop_url
    
    return posters, backdrops


# Serve Recommendations 
def recommend(movie_titles, num_recommendations=6):
    if not isinstance(movie_titles, list):
        movie_titles = [movie_titles]

    recommendations = []
    for movie_title in movie_titles:
        try:
            index = movies[movies['title'] == movie_title].index[0]
        except IndexError:
            continue

        distances = list(enumerate(similarity[index]))
        sorted_distances = sorted(distances, reverse=True, key=lambda x: x[1])

        for i in sorted_distances[1:num_recommendations + 1]:
            movie = movies.iloc[i[0]]
            recommendations.append({
                'title': movie.title,
                'certificate': movie.certificate,
                'id': movie.id,
                'genre': movie.genre,
                'rating': movie.rating,
                'release_date': movie.release_date,
                'overview': movie.overview
            })

    unique_recommendations = {rec['id']: rec for rec in recommendations}.values()
    return list(unique_recommendations)


# Get Random/Top Movies
def get_random_movies(num_movies):
    random_indices = rd.sample(range(len(top_movies_df)), num_movies)
    random_movies_df = top_movies_df.iloc[random_indices]
    movie_ids = random_movies_df['id'].tolist() 
    posters, _ = asyncio.run(fetch_posters(movie_ids))

    random_movies = []
    for movie in random_movies_df.itertuples():
        random_movies.append({
            'id': movie.id,
            'title': movie.title,
            'poster_url': posters.get(movie.id)})
    return random_movies