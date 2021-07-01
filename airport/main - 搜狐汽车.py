import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,50):
    post_url = "https://v2.sohu.com/public-api/feed?callback=jQuery18305615274057044433_1624904746043&subId=0&scene=CHANNEL&sceneId=18&page="+str(i)+"&size=12&context%5Bname%5D=news&_=1624904768999"
    #while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
    filename = '[搜狐汽车]'+str(i)+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
        #os.system("scrapy crawl wenzhou")
    print("load data success! ",i)
    time.sleep(2)
    #time.sleep(3600*24) # 每24小时爬一次