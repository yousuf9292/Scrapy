import scrapy
from .. items import AmaItem
class Amazon(scrapy.Spider):
    name='amazon'
    start_urls=['https://www.foodpanda.pk/']

    def parse(self,response):
        all_city=response.css(".city-list a::attr(href)").getall()
        for city in all_city:
            link=response.urljoin(city)

            yield scrapy.Request(url=link,callback=self.parse_data)
    
    def parse_data(self,response):
        img_urls=[]
        items=AmaItem()

        for tile in response.css(".vendor-tile"):
            image_urls=tile.css(".vendor-picture::attr(data-src)").get()
            image_urls=image_urls.split('|')[0]
            resturants=tile.css(".fn::text").getall()
            rating=tile.css(".rating strong::text").getall()
            count=tile.css("span.count::text").getall()
            img_urls.append(image_urls)
            
            yield {'resturant':resturants,
                   'rating':rating,
                   'count':count,
                   'image_url':img_urls  
                    }

        
        items['image_urls']=img_urls
        yield items