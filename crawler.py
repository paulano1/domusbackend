
from time import sleep
from turtle import update
from unicodedata import category
from urllib import response
import newspaper
from newspaper import article
import requests
import json

#this is for overall news 
class newScrapper():
    def __init__(self, categories) -> None:
        self.__categories = categories
        self.__url = []
        self.__key = "7a7c94979e8f4ad0a6d8c1848a7052e7"
        self.__responses = {

            "status": "ok",
            "totalResults" : 0,
            "articles" : []
        }
        self.__data = {
            "status" : "ok",
            "total results" : 0,
            "articles" : []
        }

    def getData(self, url):
        url_i = newspaper.Article(url="%s" % (url), language='en')
        url_i.download()
        url_i.parse()
        return url_i.text
    def parser(self, response):
        return [response["articles"][0],response["articles"][1]]

    def titleStorer(self):
        pass

    def ___updateContent(self):
        articles = self.__responses["articles"]
        for article in articles:
            url = article["url"]
            url_i = newspaper.Article(url="%s" % (url), language='en')
            
            try:
                url_i.download()
                url_i.parse()
                url_i.nlp()
            except:
                pass
            f = open("titles.json", "w")

            #sleep(10)
            temp = {
                "source" : article["source"]["name"],
                "url" : article["url"],
                "img" : article["urlToImage"],
                "time" : article["publishedAt"],
                "summary": url_i.summary.replace("\n", "").replace("\u2019", "").replace("\u2020", "").replace("\u2014", "").replace("\u201c","").replace("\u201d", "").replace("\u2013","")
            }
            self.__data["articles"].append(temp)
        
        f = open("titles.json", "w")
        
        
    def updateGeneralNews(self):
        link = "https://newsapi.org/v2/everything?q="
        rest = "&apiKey="
        
        for category in self.__categories:
            response = requests.get(link + category + rest + self.__key)
            r = self.parser(response.json())
            self.__responses["articles"].append(r[0])
            self.__responses["articles"].append(r[1])
            
        self.___updateContent()
        return 1

    def getGeneralNews(self):
         
        if (self.updateGeneralNews() == 1):
            return self.__data
    def jsonDump(self, name = "news.json"):
        with open("news.json", "w") as outfile:
            news = self.getGeneralNews()

            json.dump(news, outfile)

#to be used for AR
class gifNews():
    def __init__(self, responses) -> None:
        pass
        
#short stories
class shortstories():
    def __init__(self) -> None:
        pass



    





