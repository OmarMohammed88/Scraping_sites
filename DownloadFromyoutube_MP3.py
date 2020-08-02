import sys
from selenium import webdriver
import time
import re
from fake_useragent import UserAgent
ua = UserAgent()
a = ua.random
user_agent = ua.random

def download_song(url):
    url=re.sub("youtube","yout",url)
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_class_name("btn.btn-primary.btn-block.btn-yout.btn-recorder").click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument(f'user-agent={user_agent}')

driver =webdriver.Chrome(r'/home/omarmohamed/myprojectdir/chromedriver',chrome_options=chrome_options)
download_song(sys.argv[1])
time.sleep(100)
driver.close()
