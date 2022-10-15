from cgitb import text
import json
from collections import Counter
import requests
import re
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
class wordlist():
    def __init__(self) -> None:
        
        self.__words = []
        self.__data = []

    def ProperNounExtractor(self, text):
    
        print('PROPER NOUNS EXTRACTED :')
        nouns = []
        sentences = nltk.sent_tokenize(text)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            words = [word for word in words if word not in set(stopwords.words('english'))]
            tagged = nltk.pos_tag(words)
            for (word, tag) in tagged:
                if tag == 'NNP': # If the word is a proper noun
                    nouns.append(word)
        return nouns
    def getList(self, query):
        self.__words = []
        for i in query:
            self.__words.append(i[0])
        return self.__words
    def generateWordList(self, flag = 0, count = 40):
        with open('news.json') as json_file:
            data = json.load(json_file)
            
        text = ""
        articles = data["articles"]
        for article in articles: 
            text += " " + article["summary"]
        
        split_it = self.ProperNounExtractor(text)
        Counters_found = Counter(split_it)
        most_occur = Counters_found.most_common(count)
        self.getList(most_occur)
        if (flag !=  0):
            return self.__words
      
    def getClues(self):
        for word in self.__words:
            resp = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
            d = resp.json()
            
            try:
                clue = d[0]["meanings"][0]["definitions"][0]["definition"]
                self.__data.append([word, clue])
            except:
                pass
        #self.__data
    def wordlistGenerator(self):
        self.generateWordList()
        self.getClues()
        return self.__data



    def printer(self):
        pass


abc = wordlist()
print(abc.wordlistGenerator())
