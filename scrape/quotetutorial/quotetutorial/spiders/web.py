import scrapy
from ..items import  QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]
    def parse(self,response):
        items=QuotetutorialItem()
        all_div=response.css("div.quote")

        for quote in all_div:
            title=quote.css("span.text::text").extract()
            author=quote.css("small.author::text").extract()

            items['title']=title
            items['author']=author

            yield items

        next_page=response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)



