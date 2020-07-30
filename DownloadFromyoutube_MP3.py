import sys
import os 
from bs4 import BeautifulSoup
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pymongo import MongoClient
from collections.abc import Iterable
import warnings
import time
import requests
import urllib.request as urllib2
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
import selenium.common.exceptions
from PIL import Image
import requests
from io import BytesIO
import cv2 
import re
import random
from langdetect import detect
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
ua = UserAgent()
a = ua.random
user_agent = ua.random

def download_song(url):
    url=re.sub("youtube","yout",url)
    driver.get(url)
#    formatTomp3_button=driver.find_element_by_class_name("btn.btn-primary.btn-block.btn-yout.btn-recorder").click()
#    time.sleep(1)
#    button_128kb_=driver.find_element_by_class_name("search-record").click()
#    time.sleep(1)
#    go_tovideo_page=driver.find_element_by_class_name("btn.btn-default.to-video-page").click()
    time.sleep(1)
    download_button=driver.find_element_by_class_name("btn.btn-primary.btn-block.btn-yout.btn-recorder").click()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument(f'user-agent={user_agent}')

driver =webdriver.Chrome(r'/home/omarmohamed/myprojectdir/chromedriver',chrome_options=chrome_options)
download_song(sys.argv[1])
time.sleep(100)
driver.close()
