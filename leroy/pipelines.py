from itemadapter import ItemAdapter
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
import hashlib
from scrapy.utils.python import to_bytes


class LeroyPipeline:
    def __init__(self):
        self.client = MongoClient("localhost:27017")
        self.db = self.client["leroy"]

    def process_item(self, item, spider: scrapy.Spider):
        self.db[spider.name].update_one({'url': {"$eq": item["url"]}}, {'$set': item}, upsert=True)
        return item


class LeroyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photo']:
            for photo_url in item['photo']:
                try:
                    yield scrapy.Request(photo_url)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photo'] = [itm[1] for itm in results]
        return item

    def file_path(self, request, response=None, info=None, *, item=None):
        image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        return f'full/{item["search"]}/{item["name"]}/{image_guid}.jpg'
