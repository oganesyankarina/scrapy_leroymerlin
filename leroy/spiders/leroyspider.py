import scrapy
from scrapy.http import HtmlResponse
from leroy.items import LeroyItem
from scrapy.loader import ItemLoader


class LeroyspiderSpider(scrapy.Spider):
    name = 'leroyspider'
    allowed_domains = ['leroymerlin.ru']
    main_url = 'https://leroymerlin.ru'

    def __init__(self, search):
        super(LeroyspiderSpider, self).__init__()
        self.search = search
        self.start_urls = [f'https://leroymerlin.ru/search/?q={self.search}']

    def parse(self, response: HtmlResponse):
        links = response.xpath('//a[contains(@data-qa, "product-name")]/@href').getall()
        for link in links:
            yield response.follow(self.main_url + link, callback=self.process_item)

        next_page = response.xpath('//a[contains(@data-qa-pagination-item, "right")]/@href').get()
        if next_page:
            yield response.follow(self.main_url + next_page, callback=self.parse)

    def process_item(self, response: HtmlResponse):
        loader = ItemLoader(item=LeroyItem(), response=response)
        loader.add_xpath('name', '//h1//text()')
        loader.add_xpath('photo', '//img[contains(@slot, "thumbs")]/@src | //img[contains(@alt, "product image")]/@src')
        loader.add_value('url', response.url)
        loader.add_xpath('price', '//span[contains(@slot,"price")]/text()')
        loader.add_xpath('characteristics', '//div[contains(@class, "def-list__group")]')
        loader.add_value('search', self.search)
        yield loader.load_item()
