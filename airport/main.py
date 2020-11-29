import requests
import time
import re
import datetime
import json
import os

se = requests.session()

post_url = "http://121.40.33.186:12800/services/wzairAuto/arrival?callback=jsonp1606647111005&_=1606647111010"
while True:
    ti = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = '[温州机场]'+ti+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
    # os.system("scrapy crawl pkx")
    # os.system('')
    print("load data success! ",ti)
    time.sleep(3600*24)