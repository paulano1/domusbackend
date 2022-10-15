from crawler import newScrapper



categories = ["Business","Cars","Entertainment","Family","Health","Politics","Religion","Science"]

news = newScrapper(categories=categories)
news.jsonDump()
