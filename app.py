from flask import Flask, request, jsonify, render_template, url_for, redirect, flash
import pandas as pd
import requests, json
import data as nf
import time
import imdb
from dotenv import load_dotenv
import os
import image
from thefuzz import fuzz
import webbrowser

load_dotenv()
omdb_key = os.getenv("OMDB_KEY")
app = Flask(__name__)
df = pd.read_csv("netflix_titles.csv")
df.drop("director", axis=1, inplace=True)
df.dropna(inplace=True)
df.reset_index()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/rec", methods=["GET", "POST"])
def recommend():
    if request.method == "POST":
        user_input = request.form["user_input"]
        # images= ['https://image.tmdb.org/t/p/original/wigZBAmNrIhxp2FNGOROUAeHvdh.jpg']*10
        # names =['Black Mirror','You','The Witcher','The Crown','The Queen\'s Gambit','Black Mirror','You','The Witcher','The Crown','The Queen\'s Gambit']
        # match to closest title
        df = pd.read_csv("all_titles.csv")
        titles = df.title.to_list()
        scores = []
        for i in titles:
            scores.append(fuzz.ratio(user_input, i))
        if max(scores) < 70:
            return render_template("error.html")
        user_input = titles[scores.index(max(scores))]
        try:
            recs = nf.recommend(user_input)
        except:
            return render_template("error.html")
        images = []
        names = []
        print(recs)
        for i in recs:
            try:
                img_url = "https://image.tmdb.org/t/p/original"
                data = imdb.get_info(i)
                images.append(img_url + data["poster_path"])
            except:
                try:
                    url = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_key, i)
                    response = requests.get(url)
                    data = response.json()
                    images.append(data["Poster"])
                except:
                    images.append(image.get_image(i))
            names.append(i)
        return render_template(
            "recs.html", user_input=user_input, images=images, names=names
        )
    else:
        images_temp = [
            "https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_SX300.jpg",
            "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
            "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
            "https://m.media-amazon.com/images/M/MV5BMDNkOTE4NDQtMTNmYi00MWE0LWE4ZTktYTc0NzhhNWIzNzJiXkEyXkFqcGdeQXVyMzQ2MDI5NjU@._V1_SX300.jpg",
        ]
        names = ["Breaking Bad", "The Matrix", "The Dark Knight", "The Office"]
        return render_template("main.html", images=images_temp, names=names)


@app.route("/info/<name>")
def info(name):
    try:
        url = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_key, name)
        response = requests.get(url)
        data = response.json()
        year = data["Year"]
        rated = data["Rated"]
        genre = data["Genre"]
        writer = data["Writer"]
        actor = data["Actors"]
        plot = data["Plot"]
        rating = data["imdbRating"]
        link = "https://www.imdb.com/title/{}".format(data["imdbID"])
        poster = data["Poster"]
    except:
        return render_template("error.html")
    # n=name,y=year,r=rated,g=genre,w=writer,a=actor,p=plot,ra=rating,s=seasons,po=poster

    return render_template(
        "info.html",
        n=name,
        y=year,
        r=rated,
        g=genre,
        w=writer,
        a=actor,
        p=plot,
        ra=rating,
        po=poster,
        link=link,
    )


if __name__ == "__main__":
    webbrowser.open("http://localhost:8080")
    app.run(host="localhost", port=8080, debug=True)
