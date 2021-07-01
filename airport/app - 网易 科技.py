from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
filename = '[科技]' + ti + '.txt'
with open(filename,"w", encoding="utf-8") as f:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='chromedriver',
        options=chrome_options)
    for i in range(2,10):
        driver.get('http://tech.163.com/special/gd2016_0'+str(i)+'/')
        time.sleep(5)
        li = driver.find_elements_by_xpath("//ul[@id='news-flow-content']/li")
        for i in li:
            print(i.text)
        for i in li:
            f.write(i.text)
    for i in range(11,20):
        driver.get('http://tech.163.com/special/gd2016_'+str(i)+'/')
        time.sleep(5)
        li = driver.find_elements_by_xpath("//ul[@id='news-flow-content']/li")
        for i in li:
            print(i.text)
        for i in li:
            f.write(i.text)
driver.close()
