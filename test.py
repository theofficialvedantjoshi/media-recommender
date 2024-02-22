import requests
from bs4 import BeautifulSoup
import re
# url = "https://api.themoviedb.org/3/tv/0903747?language=en-US".format(id)
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YzA3ZTkwN2U0YWViM2M1ZDhkZTNhYmNmNzg3NWYwMyIsInN1YiI6IjY1NThlZGUyN2YwNTQwMThkNmYzYzgyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNHiqLgWTsgtJS_h9S7NvURxAJR5Jf0FjQqFmMvm6UE"
# }
# response = requests.get(url, headers=headers)
# data = response.json()
# print(data)
url = "https://www.themoviedb.org/search?query=breaking bad"
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
id = soup.find('div',class_="title").find('a',href=True)['href']
id = re.findall(r'\d+',id)[0]

