
import os
from os import link, stat
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import math
import requests
import newspaper
import json
key = os.environ.get('API')
from bs4 import BeautifulSoup

app = FastAPI()





@app.get("/")
def hello():
    return {"message":"its running"}

@app.get('/get/news',status_code=200)
def get_posts():
    f = open('news.json')
    data = json.load(f)
    return (data)
@app.get('/get/pred',status_code=200)
def getPredposts():
    f = open('pred.json')
    data = json.load(f)
    return {"pred" : data["predictiveNews"]}

@app.get('/get/jokes',status_code=200)
def getPredposts():
    f = open('pred.json')
    data = json.load(f)
    return {"jokes" : data["jokes"]}

@app.get('/get/shortstories',status_code=200)
def getStoriesposts():
    f = open('pred.json')
    data = json.load(f)
    return {"stories" : data["shortStories"]}

@app.get('/get/top100',status_code=200)
def getTop100(): 
    URL = "https://www.billboard.com/charts/hot-100/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    uls = soup.find_all("ul", "o-chart-results-list-row")
    songs = []
    for ul in uls:
        songName = ul.find_all("h3")[0].text.strip()
        artist = ul.find_all("span","u-max-width-330")[0].text.strip()
        json={
            "name":songName,
            "artist":artist
        }
        songs.append(json)
    return songs