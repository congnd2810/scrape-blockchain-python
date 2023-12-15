from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time
from bs4 import BeautifulSoup

weburl = 'https://marginatm.com/menu/tin-tuc-bitcoin'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.set_page_load_timeout(10)
driver.get(weburl)

listArticales = []

while True:
    articles = driver.find_elements(
        By.CSS_SELECTOR, "#layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div ")
    for a in articles:
        urlArticle = a.find_element(By.CSS_SELECTOR, "div a")
        newUrl = urlArticle.get_attribute('href')
        listArticales.append(newUrl)
    break
