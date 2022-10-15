
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
from crawler import wordlist
from bs4 import BeautifulSoup
key = os.environ.get('API')

app = FastAPI()




@app.get("/")
def hello():
    return {"message":"its running"}

@app.get('/get/news',status_code=200)
def get_posts():
    f = open('news.json')
    data = json.load(f)
    return (data)

@app.get('/get/crossword',status_code=200)
def get_posts():
    f = open('legend.json')
    data = json.load(f)
    return (data)
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
@app.post('/post/properNouns', status_code = status.HTTP_201_CREATED )
def create_posts(new :  dict):
    abc  = wordlist()
    return {"proper": abc.ProperNounExtractor(new['text'])}
    