import requests
import time
import re
import datetime
import json
import os

se = requests.session()
post_url = "https://interface.sina.cn/news/get_news_by_channel_new_v2018.d.json?cat_1=70035&level=1,2&page=4&show_num=200&callback=jQuery191013256647717961534_1624899120134&_=1624899120137 "
#while True:
ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
filename = '[军事]'+ti+'.txt'
data = se.get(post_url).text#.replace("'", '"').replace('/ ', '/')
print(data.encode('utf-8').decode('unicode_escape'))
with open(filename,"wb",) as f:
    f.write(data.encode('utf-8').decode('unicode_escape').encode('utf-8'))
    #os.system("scrapy crawl wenzhou")
print("load data success! ",ti)
    #time.sleep(3600*24) # 每24小时爬一次