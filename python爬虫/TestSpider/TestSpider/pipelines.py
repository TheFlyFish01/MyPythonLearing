# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TestspiderPipeline:
    def __init__(self):
        #打开json文件
        self.file_json = open('movie.json','wb')
        self.file_txt = open('movie.txt','a',encoding='utf-8')
    def process_item(self, item, spider):
        #保存文件
        if item['title'] != None:
            data = json.dumps(dict(item), ensure_ascii=False, indent=4) + ','
            self.file_json.write(data.encode('utf-8'))
            self.file_txt.write("%s  https://mmy.la/%s\n"%(item["title"],item["url"]))
        return item
        #关闭文件
    def close_spider(self,spider):
        self.file_json.close()
        self.file_txt.close()
    
