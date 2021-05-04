import scrapy
from scrapy.loader.processors import TakeFirst, Compose
from scrapy.http import HtmlResponse


def process_price(price):
    try:
        price = int(price[0].replace(" ", ""))
        return price
    except Exception as e:
        print(e)


def process_characteristics(url):
    characteristics = {}
    for el in url:
        response = HtmlResponse(url="HTML", body=el, encoding='utf-8')
        key = response.xpath('//dt[contains(@class,"def-list__term")]/text()').get()
        value = response.xpath('//dd[contains(@class,"def-list__definition")]/text()').get()
        value = value.strip()
        characteristics[key] = value
    return characteristics


class LeroyItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field()
    characteristics = scrapy.Field(input_processor=Compose(process_characteristics), output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(input_processor=Compose(process_price), output_processor=TakeFirst())
    search = scrapy.Field(output_processor=TakeFirst())
