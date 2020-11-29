# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import json

class AirportPipeline:
    def __init__(self):
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        filename = '[温州机场]'+time+'.json'
        self.file = open(filename, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item
