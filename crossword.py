from cgitb import text
import json
from collections import Counter

class crossword():
    def __init__(self, gridsize) -> None:
        self.__grid = [[]*gridsize]*gridsize

    def generateWordList(self):
        f = open("news.json", "w")
        data = json.load(f)
        articles = data["articles"]
        for article in articles: 
            text += " " + article["summary"]
        split_it = text.split()
        Counters_found = Counter(split_it)
        most_occur = Counters_found.most_common(10)
        print(most_occur)


    def printer(self):
        pass


abc = crossword(9)
abc.generateWordList()
