# 爬虫使用说明

### 环境配置方法

- Scrapy

```
pip install Scrapy
scrapy startproject airport
cd airport # 进入项目airport目录
scrapy genspider wenzhou http://www.wzair.cn/lkfw/hbxx/jrdg/index.html?v=1606439135598&rxLoad=1&_rand=1606586459057
```

- selenium

[见教程：爬取动态渲染网站](https://sunflowercoder.com/Scrapy-Selenium%E7%88%AC%E5%8F%96%E5%8A%A8%E6%80%81%E6%B8%B2%E6%9F%93%E7%BD%91%E7%AB%99/)

### 代码运行说明

在外层airport文件夹下，输入以下命令，即可运行（每24h爬取一次数据）

```bash
python main.py # 使用python 3版本
```

## 实验过程

一开始，我使用scrapy框架进行爬取，发现自xpath中自//table后，便无法获得向下节点的对应信息。于是，我考虑了用以下两种方式来爬：

- 获取API
- selenium模拟网页行为爬取

### 通过API

```python
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
    filename = '[数据]'+ti+'.json'
    data = se.get(post_url).text.replace("'", '"').replace('/ ', '/')
    with open(filename,"w", encoding="utf-8") as f:
        f.write(data)
    # os.system("scrapy crawl wenzhou")
    print("load data success! ",ti)
    time.sleep(3600*24) # 每24小时爬一次
```

### 通过selenium

在`airport/app.py`中，代码如下：

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='chromedriver',
    options=chrome_options)
driver.get('http://www.wzair.cn/lkfw/hbxx/jrdg/index.html?v=1606439135598/')
time.sleep(5)
li = driver.find_elements_by_xpath("//td[@id='hangbanInfoBox']/table/tbody/tr")
for i in li:
    print(i.text)
driver.close()
```

## 数据相关

### API法

#### 数据截图

![image-20210714121124696](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210714121124696.png)

### selenium法

#### 数据截图

![image-20210714121145335](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20210714121145335.png)

