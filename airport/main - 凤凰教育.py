import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,2):
    post_url = "https://shankapi.ifeng.com/shanklist/_/getColumnInfo/_/default/6810538632542163237/1623760339000/20/18-/getColumnInfoCallback?callback=getColumnInfoCallback&_=16249055071193"
    #while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
    filename = '[搜狐教育]'+str(i)+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
        #os.system("scrapy crawl wenzhou")
    print("load data success! ",i)
    time.sleep(2)
    #time.sleep(3600*24) # 每24小时爬一次