import requests
import time
import re
import datetime
import json
import os

se = requests.session()
for i in range(1,100):
    post_url = "https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=ent&srv_id=pc&offset="+str(20*i)+"&limit=20&strategy=1&ext={%22pool%22:[%22high%22,%22top%22],%22is_filter%22:10,%22check_type%22:true}"
    #while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
    filename = '[腾讯娱乐]'+str(i)+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
        #os.system("scrapy crawl wenzhou")
    print("load data success! ",i)
    time.sleep(2)
    #time.sleep(3600*24) # 每24小时爬一次