import  scrapy
from .. items import DocItem

class Tut(scrapy.Spider):
    name='quote'
    start_urls=[
        'https://priceoye.pk/fridge/changhongruba',
        'https://priceoye.pk/fridge/dawlance',
        'https://priceoye.pk/fridge/haier',
        'https://priceoye.pk/fridge/pel',
        'https://priceoye.pk/fridge/orient'
        ]
    
    def parse(self,response):
        items=DocItem()
        img_urls=[]
        for div in response.css("div.productBox"):
            image_urls=div.css("img::attr(src)").get()
            img_urls.append(image_urls)
        items["image_urls"]=img_urls
        yield items

        next_page=response.css("div.pagination a::attr(href)")[-2].get()
        
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)



            
            

