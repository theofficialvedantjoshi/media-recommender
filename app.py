from flask import Flask, request, jsonify, render_template,url_for,redirect,flash
import pandas as pd
import requests,json
import data as nf
import time
import imdb 
app = Flask(__name__)
df = pd.read_csv('netflix_titles.csv')
df.drop('director', axis=1, inplace=True)
df.dropna(inplace=True)
df.reset_index()
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
@app.route('/data')
def index():
    return render_template('data.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
@app.route('/rec', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        user_input = request.form['user_input']
        images= ['https://image.tmdb.org/t/p/original/wigZBAmNrIhxp2FNGOROUAeHvdh.jpg']*10
        names =['Black Mirror','You','The Witcher','The Crown','The Queen\'s Gambit','Black Mirror','You','The Witcher','The Crown','The Queen\'s Gambit']
        # try:
        #     recs = nf.recommend(user_input)
        # except:
        #     images_temp=["https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_SX300.jpg"
        #         ,"https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"
        #         ,"https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg"
        #         ,"https://m.media-amazon.com/images/M/MV5BMDNkOTE4NDQtMTNmYi00MWE0LWE4ZTktYTc0NzhhNWIzNzJiXkEyXkFqcGdeQXVyMzQ2MDI5NjU@._V1_SX300.jpg"
        # ]
        #     return render_template('error.html')
        # images=[]
        # names =[]
        # print(recs)
        # for i in recs:
        #     try:
        #         img_url = 'https://image.tmdb.org/t/p/original'
        #         data = imdb.get_info(i)
        #         images.append(img_url+data['poster_path'])
        #     except:
        #         images.append("https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_SX300.jpg")
        #     names.append(i)
        return render_template('recs.html', user_input=user_input,images=images,names=names)
    else:
        images_temp=["https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_SX300.jpg"
                ,"https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"
                ,"https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg"
                ,"https://m.media-amazon.com/images/M/MV5BMDNkOTE4NDQtMTNmYi00MWE0LWE4ZTktYTc0NzhhNWIzNzJiXkEyXkFqcGdeQXVyMzQ2MDI5NjU@._V1_SX300.jpg"
        ]
        return render_template('main.html',images=images_temp)
@app.route('/info<name>')
def info(name):
    url = "http://www.omdbapi.com/?apikey=e64b4ef4&t={}".format(name) 
    response = requests.get(url)
    data = response.json()
    year = data['Year']
    rated = data['Rated']
    genre = data['Genre']
    writer = data['Writer']
    actor = data['Actors']
    plot = data['Plot']
    rating = data['imdbRating']
    try:
        seasons = data['totalSeasons']
    except:
        seasons = 'N/A'
    poster = data['Poster']
    #n=name,y=year,r=rated,g=genre,w=writer,a=actor,p=plot,ra=rating,s=seasons,po=poster
    
    return render_template('info.html',n=name,y=year,r=rated,g=genre,w=writer,a=actor,p=plot,ra=rating,s=seasons,po=poster)

if __name__ == '__main__':
    app.run(host="localhost",port=8080,debug=True)
