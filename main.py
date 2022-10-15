
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

@app.post('/prob', status_code = status.HTTP_201_CREATED )
def create_posts(new :  dict):
    
    return {
        "probability" : str(prob(new))
    }