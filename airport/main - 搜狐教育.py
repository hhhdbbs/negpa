import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,100):
    post_url = "https://v2.sohu.com/integration-api/mix/region/10459?size=25&adapter=pc&secureScore=50&page="+str(i)+"&pvId=1624904960865WjOnvKl&requestId=1620743460366d6v4f1_1624904969313&callback=jQuery112403112096595057885_1624904960635&_=1624904960638"
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