
import os
from os import link, stat, path
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import math
import requests
import newspaper
import json
from crawler import newScrapper

key = os.environ.get('API')

app = FastAPI()


categories = ["Business","Cars","Entertainment","Family","Health","Politics","Religion","Science"]


@app.get("/")
def hello():
    return {"message":"its running"}

@app.get('/news/general',status_code=200)
def get_posts():
    try:
        f = open('news.json')
    except: 
        news = newScrapper(categories=categories)
        news.jsonDump()
    data = json.load(f)
    return (data)

@app.get('/news/predictive', status_code=200)
def get_posts():
    try:
        f = open('predictiveNews.json')
    except: 
        news = newScrapper(categories=categories)
        news.jsonDump()
    data = json.load(f)
    return (data)




@app.post('/prob', status_code = status.HTTP_201_CREATED )
def create_posts(new :  dict):
    
    return {
        "probability" : str(prob(new))
    }

