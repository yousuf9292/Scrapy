import scrapy
# import cv2 
from ..items import AnotherItem

class Another(scrapy.Spider):
    name='another'

    start_urls=['https://www.dawn.com/magazines']

    def parse(self,response):
        items=AnotherItem()
        img_urls=[]
        for div in response.css("article"):
            N_heading=div.css("a::text")[0].getall()
            image_urls=div.css("img::attr(src)").get()
            img_urls.append(image_urls)
            N_author=div.css("a::text")[1].getall()
            N_paragraph=div.css("p::text").getall()
            N_date=div.css("span.timestamp__calendar::text").getall()
            yield {
                'NEWS_HEADINGS':N_heading,
                'NEWS_AUTHOR':N_author,
                'NEWS_PARAGRAPH':N_paragraph,
                'PUBLISHED_DATE':N_date,
                'URLS':image_urls
                    }
        items["image_urls"]=img_urls
        yield items
            




        
