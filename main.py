
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
from crosswords import generator

key = os.environ.get('API')

app = FastAPI()



categories = ["Business","Cars","Entertainment","Family","Health","Politics","Religion","Science"]


@app.get("/get/news")
def hello():
    with open('news.json') as json_file:
        data = json.load(json_file)
    
    return data

@app.get('get/news/general',status_code=200)
def get_posts():
    '''try:
        f = open('news.json')
    except: 
        
    data = json.load(f)
    return (data)'''
    pass

    
@app.get("/get/crossword")
def getCrossword():
    with open('legend.json') as json_file:
        data = json.load(json_file)
    
    return data
    

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
        "probability" : "down"
    }

