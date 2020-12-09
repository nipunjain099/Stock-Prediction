import scrapy
from scrapy.http import Request

#globvar = 0
class NewsItem:
    def __init__(self):
        self.date = '1'
        self.url = 'a'

class BrickSetSpider(scrapy.Spider):
    name = "tata_motors_news_spider"
    #start_urls = ['https://www.reuters.com/finance/stocks/company-news/AAPL.OQ?date=11302017']
    

    def start_requests(self):
        global globvar
        for year in range(2012, 2013):
            y = year
            for month in range(1, 2):
                if month < 10 :
                    m = '0' + str(month)
                else :
                    m = month
                for days in range(1, 32):
                    if days < 10: 
                        d = '0' + str(days)
                    else :
                        d = days
        
                    yield self.make_requests_from_url('https://www.google.com/search?q=tata+motors&biw=1366&bih=657&source=lnt&tbs=cdr%%3A1%%2Ccd_min%%3A%s%%2F%s%%2F%s%%2Ccd_max%%3A%s%%2F%s%%2F%s&tbm=nws'% (m, d, y, m, d, y))

    def parse(self, response):
        NEWS_SELECTOR = 'div div div' #grab all news
        items= []
        for news in response.css(NEWS_SELECTOR):
            HEAD_SELECTOR = 'h2 a ::text'
            CONTENT_URL_SELECTOR = 'a::attr(href)'
            cururl = response.url
            furl = news.css(CONTENT_URL_SELECTOR).extract_first()
            if(furl is None or furl[1:4] != "url"):
              continue
            yield {
                'date' : cururl,
                'url' : furl,

            }


