from click import prompt
import requests
from words import wordlist
import random
import os


class Predictive():
    def __init__(self) -> None:
        self.__mood = ["Night", "Dusk", "Dawn", "Spring", "Fall", "Falling leaves", "Cloudless", "Midnight"]
        self.__names = ["John", "Jessica", "Daniel",  "Emily", "Amilia", "Paul", "Jason"]
        abc = wordlist()
        self.__words = abc.generateWordList(flag=1,count=5)
        self.___futureWords = ["3D printed food", "decrease in global warming", "decrease in greenhouse gases", "future of healthy eating", "floating cities", "flying cars", "renewable energy", "Sustainable city", "Robots", "artificial intelligence", "universal basic income", "electric vehicles"]

    def getWords(self):
        return self.__words
    
    def getImages(self, text):
        key = os.getenv(key='OPENAI')
        header = {
            "Authorization": key
        }
        response = requests.get("https://api.pexels.com/v1/search?query="+text+"&per_page=1", headers=header)
        return (response.json()["photos"][0]["src"]["original"])

    def getShortStory(self):
        temp = ""
        for word in self.__words:
            temp += word
            temp += ", "
        mood = random.choice(self.__mood)
        string = "" + random.choice(self.__names) + ", "+ random.choice(self.__names) + ", "+ temp + mood
        prompt = "Generate a story with " + string
        pred = self.GPTrequest(prompt=prompt)
        img = self.getImages(mood)
        '''if (len(pred) < 1000):
            final_pred = self.GPTrequest(pred)
            return {"story" : final_pred,
                    "img" : ""}
        else:'''
        return {"story" : pred.replace("\n", ""),
                    "img" : img}

    def getPredictiveNews(self):
        core = random.choice(self.___futureWords)
        string = "" + core + ", "+ random.choice(self.___futureWords) + ", "+ random.choice(self.___futureWords) + ", "+ random.choice(self.___futureWords) + ", "+ random.choice(self.___futureWords) + ", "
        prompt = "Generate a positive news article from the year 2070 with the keywords" + string
        pred = self.GPTrequest(prompt=prompt)
        img = self.getImages(core)
        if (len(pred) < 1000):
            final_pred = self.GPTrequest(pred)
            return {"futureNews" : final_pred.replace("\n", "")}
        else:
            return {"futureNews" : pred.replace("\n", "")}
    
    def getJokes(self, artists = ["Kendrik Lamar", "Taylor Swift", "Ed Sheeran", "Daft Punk"]):
        prompt = "make jokes on " + random.choice(artists)
        pred = self.GPTrequest(prompt=prompt)
        return {"jokes" : pred.replace("\n", "")}

    
    def GPTrequest(self, prompt):
        url = "https://api.openai.com/v1/completions"
        key = "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"
        headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
            'Authorization': 'Bearer '+key,
        }

        json_data = {
            'model': 'text-davinci-002',
            'prompt': prompt,
            'max_tokens': 4000,
            'temperature': 0,
        }
        response = requests.post(url, headers=headers, json=json_data)  
        data=response.json()
        predictive = data["choices"][0]["text"]
        #print(data["choices"])
        #print(predictive)
        return predictive




abc = predictive()
print(abc.getJokes())
