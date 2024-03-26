from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
import time
from bs4 import BeautifulSoup

weburl = 'https://marginatm.com/menu/gamefi'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options)
driver.set_page_load_timeout(10)
driver.get(weburl)

wait = WebDriverWait(driver, 10)

articles = driver.find_elements(
    By.CSS_SELECTOR, "#layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div ")

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
           "#layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div:nth-child(12)")))
articlesLength = 0
listUrlArticales = []
count = 0
while True:
    cssSelector = f"#layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div:nth-child(24)"
    #channel-body > div > div > div.flex.flex-wrap
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
    articles = driver.find_elements(
        By.CSS_SELECTOR, "#layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div ")
    if len(articles) > articlesLength:
        articlesLength = len(articles)
    else:
        break
    # while True:
    #     if len(articles) > articlesLength:
    #         articlesLength = len(articles)
    #         break
    #     else:
    #         time.sleep(0.5)
    count += 1

for a in articles:
    urlArticle = a.find_element(By.CSS_SELECTOR, "div a")
    newUrl = urlArticle.get_attribute('href')
    listUrlArticales.append(newUrl)

tintucbtc = {'articels': listUrlArticales}
print(len(listUrlArticales))

fjson = open(f'./Kiếm Tiền/GameFi.json', 'w', encoding='utf-8')

jsonQ = json.dumps(tintucbtc, indent=2)

fjson.write(jsonQ)

driver.quit()

# layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div:nth-child(3)
# layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div:nth-child(4)
# layout-normal-minHeight > main > div:nth-child(2) > div > div.style_customRow__l_Y1O.row > div:nth-child(18)
