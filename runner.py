from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leroy import settings
from leroy.spiders.leroyspider import LeroyspiderSpider
from urllib.parse import quote_plus

if __name__ == "__main__":
    search = input("Что ищем?: ")
    # search = quote_plus(search.encode("utf-8"))

    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroyspiderSpider, search=search)

    process.start()
