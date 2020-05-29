import scrapy 
from.. items import TableItem

class Scrape(scrapy.Spider):
    name='tables'

    start_urls=["http://pokemondb.net/pokedex/all"]

    def parse(self,response):
        for tr in response.css("tr"):
            for td in tr.css("td"):
                num=tr.css(".infocard-cell-data::text").getall()
                name=tr.css(".ent-name::text").getall()
                types=tr.css(".cell-icon a::text").getall()
                total=tr.css(".cell-total::text").getall()
                hp=tr.css(".cell-num::text")[0].getall()
                attack=tr.css(".cell-num::text")[1].getall()
                defense=tr.css(".cell-num::text")[2].getall()
                speed_atk=tr.css(".cell-num::text")[3].getall()
                speed_defense=tr.css(".cell-num::text")[4].getall()
                speed=tr.css(".cell-num::text")[5].getall()
                image_urls=tr.css(".infocard-cell-img span::attr(data-src)").getall()
                yield {
                    '#':num,
                    'Name':name,
                    'Type':types,
                    'Total':total,
                    'Hp':hp,
                    'Attack':attack,
                    'Defense':defense,
                    'Speed_Atk':speed_atk,
                    'Speed_Defense':speed_defense,
                    'Speed':speed,
                    'Image_urls':image_urls
                    }
                break