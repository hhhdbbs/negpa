import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,2):
    post_url = "https://v2.sohu.com/integration-api/mix/region/7551?page=3&size=40&pvId=1624903823022jQ9YtHS&requestId=1620743460366d6v4f1_1624903884967&callback=jQuery112406708128435806071_1624903822914&_=1624903822919"
    #while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
    filename = '[搜狐时尚]'+str(i)+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
        #os.system("scrapy crawl wenzhou")
    print("load data success! ",i)
    time.sleep(2)
    #time.sleep(3600*24) # 每24小时爬一次