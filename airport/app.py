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
