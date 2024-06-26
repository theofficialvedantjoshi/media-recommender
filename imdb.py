# import requests
# from bs4 import BeautifulSoup
# url = "https://www.imdb.com/find/?q=The%20Matrix"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.find('a', class_='ipc-metadata-list-summary-item__t', href=True)['href'])
# import requests

# import requests

# url = "https://api.themoviedb.org/3/movie/tt0133093?language=en-US"

# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YzA3ZTkwN2U0YWViM2M1ZDhkZTNhYmNmNzg3NWYwMyIsInN1YiI6IjY1NThlZGUyN2YwNTQwMThkNmYzYzgyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNHiqLgWTsgtJS_h9S7NvURxAJR5Jf0FjQqFmMvm6UE"
# }

# response = requests.get(url, headers=headers)
# data = response.json()
# print(data['poster_path'])
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
tmdb_token = os.getenv("TMDB_KEY")


def get_info(name):

    df = pd.read_csv("all_titles.csv")
    # check if movie or series
    if df[df.title == name].type.values[0] == "Movie":
        url1 = "https://www.imdb.com/find/?q={}".format(name)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url1, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        id = soup.find("a", class_="ipc-metadata-list-summary-item__t", href=True)[
            "href"
        ]
        id = re.findall(r"tt\d+", id)[0]
        url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(id)
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(tmdb_token),
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
    else:
        url = "https://www.themoviedb.org/search?query={}".format(name.lower())
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        id = soup.find("div", class_="title").find("a", href=True)["href"]
        id = re.findall(r"\d+", id)[0]
        url = "https://api.themoviedb.org/3/tv/{}?language=en-US".format(id)
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(tmdb_token),
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data
