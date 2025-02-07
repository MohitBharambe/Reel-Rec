# Reel Rec

### Reel Rec - A Movie Recommendation AI designed to change the way movie enthusiasts discover and enjoy  favorite films.

## Table of Contents
- [Overview](#overview)
- [Requirement Specifications/Tech Stack](#requirement-specifications--tech-stack)
- [Installation](#installation)
- [Screenshots](#screenshots)
- [Usage](#usage)
- [License](#license)
- [Attributions](#attributions)
- [Planned Future Updates](#planned-future-updates)
- [Contributing](#contributing)
- [Contact](#contact)

![home](https://github.com/user-attachments/assets/4e019661-b409-47b0-b6cd-40abcc26d122)

# Overview
Reel Rec is a content-based recommendation AI developed as a web application using
Django & Tailwind CSS for smooth user experience. Users also signup and receive movie recommendations by simply selecting a movie they're familiar with without restrictions on genre, actor, release date, or film industry & receive Personalized Recommendations. After receiving the recommendations, users have the option to view movie details, watch the trailer through YouTube.

## Requirement Specifications / Tech Stack
- Languages: [**Python**](https://www.python.org/downloads/), [**Javascript**](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Frameworks: [**Tailwind CSS**](https://tailwindcss.com/docs/installation/play-cdn) & [**Django**](https://www.djangoproject.com/) 
- Database: [**MySQL**](https://dev.mysql.com/downloads/)
- Libraries: [**Barba JS**](https://barba.js.org/docs/getstarted/install/) & [**GSAP**](https://gsap.com/docs/v3/Installation)
- API: [**TMDB API**](https://developer.themoviedb.org/reference/intro/getting-started)

## Installation
#### There are two ways to setup Reel-Rec on your local machine.
### 1. Easy Install using Batch Script [*Windows only*] (**Recommended**)

1. Clone the repository:

    ```sh
    git clone https://github.com/MohitBharambe/Reel-Rec.git
    ```
2. Run the following commands in the terminal:
    ```sh
    cd Reel-Rec
    install.bat
    ```
3. The Script will automatically create a virtual environment, install the required dependencies & start the app.

### 2. Manual Installation [*Windows, MacOS, Linux*] 
1. Clone the repository:

    ```sh
    git clone https://github.com/MohitBharambe/Reel-Rec.git
    cd Reel-Rec
    ```
2. Create & Activate a Virtual Environment (optional):
    ```sh
    python -m venv env # Create
    source env/bin/activate  # for MACOS
    env\Scripts\activate # for Windows
    ```
3. Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```
4. In MySQL Shell, Create a database named `reel_rec`:
    ```sql
    create database reel_rec;
    ```  
5. Create a `.env` file at the root level of the directory with the following variables and assign the respective values:
    ```python
    SECRET_KEY=<any_random_alphanumeric_key>
    MYSQL_USER=<your_mysql_user>
    MYSQL_PASSWORD=<your_mysql_password>
    bearer_token=<your_tmdb_bearer_token>
    ```
6. Inside the `Models` directory Run the `algorithm.ipynb` file Using Jupyter Notebook to generate the Model's  files.

7. Perform migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
8. Create a Admin User(optional):
    ```sh
    python manage.py createsuperuser
    ```
9. Run the server:
    ```sh
    python manage.py runserver
    ```
10. If the shell output is Similar to the one below , The app can now be accessed at `http://127.0.0.1:8000`
    ```sh
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    December 10, 2024 - 15:44:16
    Django version 5.1.4, using settings 'Reel_Rec.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    
## Screenshots
### 1 - Select familiar Movies
 ![rrec-1](https://github.com/user-attachments/assets/2e6981e9-5af1-4f59-a3ee-7aff4d88b9a1)

### 2 - Get Recommendations
![rrec-4](https://github.com/user-attachments/assets/1aab5110-59ee-44ee-b62c-9492fcffff1b)


### FAQ Page
![faq](https://github.com/user-attachments/assets/7f4579ad-e61d-4c63-881e-5010addb5a7b)

## Usage
![rrec-demonstration1](https://github.com/user-attachments/assets/c6135aca-4305-47aa-b6bc-9736b2066e5a)


## License
![License](https://img.shields.io/github/license/MohitBharambe/Reel-Rec)

This project is licensed under the MIT License. See the [``LICENSE``](https://github.com/MohitBharambe/Reel-Rec/blob/a6a15674b7f740ce16c025ded38cdd61bd155bf2/LICENSE) file for more details.

##  Attributions
<img src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_1-5bdc75aaebeb75dc7ae79426ddd9be3b2be1e342510f8202baf6bffa71d7f5c4.svg" alt="tmdb_logo" width="60"/>

This product uses the TMDB API but is not endorsed or certified by TMDB.

- [TMDB API](https://developer.themoviedb.org/reference/intro/getting-started)
- [Dataset Used ](https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k)

## Planned Future Updates
- Get Recommendations based on User's Mood.
- Add a feature to save favorite movies.

## Contributing

Thank you for considering contributing to Reel Rec! refer the [``contributing.md``](https://github.com/MohitBharambe/Reel-Rec/blob/a6a15674b7f740ce16c025ded38cdd61bd155bf2/contributing.md) file for making a contribution.

## Contact
- Github:
  
  https://github.com/MohitBharambe

- Email Address: 

  mohitbharambe0@outlook.com
