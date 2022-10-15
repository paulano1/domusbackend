
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


def par(a):
    n = {}
    for i in a.keys():
        t = a[str(i)]
        if t['inputType'] == 'input-radio':
            if t['value'] == '18-26': 
                n['1'] = 1
            elif t['value'] == 'NO':
                n[str(i)] = 0
            elif t['value'] == 'YES':
                n[str(i)] = 1
        elif t['inputType'] == 'input-text':
            n[str(i)] = t['value']

    return n  
def prob(temp):
    coef = {
    '1' : 0.79,
    '2' : 0.14,
    '3' : 0.37,
    '4' : 0.4,
    '5' : 0.26,
    '6' : 0.15,
    '7' : 0.25,
    '8' : 0.40,
    '9' : 0.14,
    '10' : 0.56,
    '11' : 0.09,
    '12' : 0.10,
    '13' : 0.17,
    '14' : 0.15,
    '15' : 0.18,
    '16' : 0.17,
    '17' : 0.19,
    '18' : 0.20,
    '19' : -0.01
}
    inp = par(temp)
    
    sub = 0
    for i in inp.keys():
        co = float(coef[i])
        dig = float(inp[i])
        
        sub = sub + (co * dig)
    total = math.e**(11.5 - (sub))
    return round(((total/(1-total))*1000),0)
    

def newsparser():
    dflt = "https://newsapi.org/v2/everything?q=health+happy&apiKey="
    link = dflt + key
    response = requests.get(link)
    news = {}
    a = response.json()
    for i in range(0,10):
        ind = {
            'source': a["articles"][i]['url'],
            'url' : a["articles"][i]['url'],
            'img' : a["articles"][i]['urlToImage'],
            'summary' : a["articles"][i]['content']
        }
        news[i] = ind
    return news

@app.get("/")
def hello():
    return {"message":"its running"}

@app.get('/news',status_code=200)
def get_posts():
    f = open('news.json')
    data = json.load(f)
    return (data)


@app.post('/prob', status_code = status.HTTP_201_CREATED )
def create_posts(new :  dict):
    
    return {
        "probability" : str(prob(new))
    }