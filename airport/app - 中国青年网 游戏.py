from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
filename = '[青年网游戏]' + ti + '.txt'
with open(filename,"w", encoding="utf-8") as f:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='chromedriver',
        options=chrome_options)
    for i in range(1,10):
        driver.get('http://youxi.youth.cn/yw/index_'+str(i)+'.htm')
        time.sleep(5)
        li = driver.find_elements_by_xpath("//ul[1]/li")
        for i in li:
            print(i.text)
        for i in li:
            f.write(i.text)

driver.close()
