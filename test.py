from crawler import newScrapper
from crosswords import generator


categories = ["Business","Cars","Entertainment","Family","Health","Politics","Religion","Science"]

news = newScrapper(categories=categories)
news.getGeneralNews()
news.jsonDump()

abc = generator()
abc.getRequest()
