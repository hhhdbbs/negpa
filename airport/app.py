from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

ti = datetime.datetime.now().strftime('%Y-%m-%d  %H-%m-%S')
filename = '[bingdu].txt'
with open(filename,"w", encoding="utf-8") as f:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='chromedriver',
        options=chrome_options)
    for i in range(1,2):
        driver.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3/')
        time.sleep(1)
        tr = driver.find_elements_by_xpath("//div[@id='nationTable']/table/tbody/tr")
        for i in tr:
            print(str(i)+i.text)
            f.write(i.text)
driver.close()