from .helpers import rd, fetch_posters,asyncio, get_random_movies
from .forms import CreateUserForm, MovieForm, ContactForm, top_movies_df

# Reel Rec's Custom Template Context Processor
def custom_context(request):
    ids = rd.sample(top_movies_df['id'].to_list(), 40)
    posters, backdrops = asyncio.run (fetch_posters(ids))
    
    sorted_backdrops = {
        'items': list(backdrops.items())
}
    # Tailwind CSS classes
    field_class = "w-full bg-gray-700 bg-opacity-50 rounded border border-gray-700 focus:border-purple-500 focus:bg-gray-900 focus:ring-2 focus:ring-purple-900 text-base outline-none text-purple-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
    button_class = "flex w-full justify-center rounded-md bg-purple-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-purple-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-purple-500 animate-this button"
    # Backdrops
    first_half = sorted_backdrops['items'][:20]
    second_half = sorted_backdrops['items'][20:40]
    
    # random or top movies
    random_movies = get_random_movies(num_movies=15)
    return {
        "posters": posters,
        "backdrops": backdrops,
        "first_half": first_half,
        "second_half": second_half,
        "form": CreateUserForm(),
        "movie_form": MovieForm(),
        "contact_form": ContactForm(),
        "random_movies": random_movies ,
        "field_class": field_class,
        "button_class": button_class
    }