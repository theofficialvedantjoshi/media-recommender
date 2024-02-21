import requests
url = "https://api.themoviedb.org/3/tv/0903747?language=en-US".format(id)
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YzA3ZTkwN2U0YWViM2M1ZDhkZTNhYmNmNzg3NWYwMyIsInN1YiI6IjY1NThlZGUyN2YwNTQwMThkNmYzYzgyMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DNHiqLgWTsgtJS_h9S7NvURxAJR5Jf0FjQqFmMvm6UE"
}
response = requests.get(url, headers=headers)
data = response.json()
print(data)
