import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,20):
    post_url = "https://house.focus.cn/baseApi/loupanSearchForIndex?cityId=1&pageSize=20&sort=6&page="+str(i)+"&t=0.8877318951938926"
    #while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
    filename = '[搜狐房产]'+str(i)+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
        #os.system("scrapy crawl wenzhou")
    print("load data success! ",i)
    time.sleep(2)
    #time.sleep(3600*24) # 每24小时爬一次