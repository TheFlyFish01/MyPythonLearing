# -*- coding: utf-8 -*-
import scrapy
from TestSpider.items import TestspiderItem

class MmyMovieSpider(scrapy.Spider):
    name = 'mmy_movie'
    allowed_domains = ['mmy.la']
    start_urls = ['https://mmy.la/forum-113-1.html']

    def parse(self, response):
        #定位title列表
        title_list = response.xpath("//*[@id='threadlisttableid']/tbody/tr/th/a[2]")
        itmes = []
        #循环找出title
        for title in title_list:
            item = TestspiderItem()
            print(title)
            print(title.xpath("./text()"))
            print(title.xpath("./text()").extract() )
            my_title = title.xpath("./text()").extract() 
            url = title.xpath("./@href").extract() 
            if my_title and url:
                item['title'] = my_title[0]
                item['url'] = url[0]
            itmes.append(item)
        return itmes
        #pass
