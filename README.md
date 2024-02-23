## Media Recommender

A full stack flask app, recommends movies and tv shows based on users input by calculating cosine similarity between text vectors of movie and tv datasets. Uses the porter stemmer algorithm to stem words into tags and cosine similarity to find the best matches.

Uses the Omdb and TMDB apis to fetch movie posters and information. The IMDB ids are scrapped directly from imdbs and tmdbs website by sending http requests and html parsing. 

Users can get recommendations, get information about movies and tv shows from a 22000+ movie dataset from Netflix, Amazon Prime , Hotstar and Hulu and visit IMDB website for more information.

Complete front end was made using pure html and css and the backend was handled by python using flask.

### Quick Start

Clone this repo and run the "pip install -r requirements. txt" in the terminal of the project directory.

Visit https://www.omdbapi.com/apikey.aspx and generate an apikey by providing your email address and activate it.

Visit https://www.themoviedb.org/ and click on the Join button enter your details. After logging in go to account settings and click on the api tab and generate an api key.

Once these steps are completed simply create a .env file in the project directory and type the following - 

OMDB_KEY = "Your Key"

TMDB_KEY ="TMDB BEARER TOKEN"

After all these steps are completed simply run the python file app.py and visit the localhost url for the website.

All the movie posters are clickable and redirect to the movies info page. Fuzzy search algorithm is implemented for the user input hence any text close to the movie title can be enetered while searching for recommendations.

If a poster for a movie does not exist or could not be scraped a default image is generated with the title of the movie in image.py and shown.

The recommendations might take time a while to load depending on the apis post speed so stay patient and wait for the results.

#### TODO

Implement the count vectorizing algorithm from scratch.

Make the code faster in terms of displaying movies.

Implement a stemming algorithm from scratch.
