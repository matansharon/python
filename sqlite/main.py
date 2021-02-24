from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# ------------------------------------------------------------------
# web_driver_path = "C:\\Users\\matca\\Desktop\\webDraiver\\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=web_driver_path)
# url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
# driver.get(url)
# basic_selector = ".lister-item-content .lister-item-header"
# all_titles_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header a")
# all_ranking_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header .lister-item-index")
# all_years_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header .lister-item-year")
# all_descriptions_temp = driver.find_elements_by_css_selector(".lister-item-content .text-muted")
# all_ratings_temp = driver.find_elements_by_css_selector(".lister-item-content .ratings-bar strong")
# all_images_temp = driver.find_elements_by_css_selector(".lister-item-image  a img")


# in all images i need to do i.get_attribute('src'))
# all_title = []
# all_ranking = []
# all_year = []
# all_descriptions = []
# all_ratings = []
# all_images=[]
# for i in all_titles_temp:
#     all_title.append(i.text)
# for i in all_ranking_temp:
#     if (i.text[1]) == '.':
#         all_ranking.append(i.text[0])
#     else:
#         all_ranking.append(i.text[0:2])
# for i in all_years_temp:
#     all_year.append(i.text[1:5])
# count = 1
# for i in all_descriptions_temp:
#     if len(i.text) > 50:
#         all_descriptions.append(i.text)
# for i in all_ratings_temp:
#     all_ratings.append(i.text)
# for i in all_images_temp:
#     all_images.append(i.get_attribute("src"))


# driver.close()
# ---------------------------------------------------------------------------------


app = Flask(__name__)

# CREATE DATABASE

# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

Bootstrap(app)
db.create_all()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
#
#
# db.create_all()

# for i in range(0,50):
#     new_movie = Movie(title=all_title[i], year=int(all_year[i]), description=all_descriptions[i],
#                       rating=float(all_ratings[i]), ranking=int(all_ranking[i]), img_url=all_images[i])
#     db.session.add(new_movie)


# db.session.commit()
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_movie():
    return render_template("add.html")


# if __name__ == '__main__':
#     app.run(debug=True)
