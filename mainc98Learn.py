from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import json
import time
from bs4 import BeautifulSoup
import os

weburl = 'https://coin98.net/learn/detail'


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options)
driver.set_page_load_timeout(10)

driver.get(weburl)
time.sleep(2)


def handleToJson(chromeDriver, filename):
    try:
        articles = []
        listUrlArticales = []
        count = 0
        articlesLength = 0
        while True:
            chromeDriver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            articles = driver.find_elements(
                By.CSS_SELECTOR, "#channel-body > div.max-w-w1440.w-full.mx-auto.relative.pt-sp200.md\:pt-1600.lg\:pt-1000.flex > div.w-full.lg\:w-\[calc\(100\%-320px\)\].pl-0.flex.justify-center.lg\:ml-auto > div > div.flex.flex-col.mx-auto.w-full.max-w-w728 > div")
            # print(len(articles))
            if len(articles) > articlesLength:
                articlesLength = len(articles)
                count += 1
            else:
                break
        for a in articles:
            urlArticle = a.find_element(By.CSS_SELECTOR, "a")
            newUrl = urlArticle.get_attribute('href')
            listUrlArticales.append(newUrl)
        # print(listUrlArticales)
        tintucbtc = {'articles': listUrlArticales}

        fjson = open(f'{filename}', 'w', encoding='utf-8')

        jsonQ = json.dumps(tintucbtc, indent=2)

        fjson.write(jsonQ)
    except:
        handleToJson(chromeDriver, filename)


'''# handle Dành cho người mới'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(4) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# handleToJson(driver, './dataCoin98/Learn/Dành cho người mới/Dành cho người mới.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(4) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

'''# dropdown Mua bán crypto'''
driver.find_element(
    By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div > button').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                "#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear")))

divMuaBanCrypto = driver.find_element(
    By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.flex.justify-between.text-text-primary.md\:hover\:cursor-pointer.items-center.px-300.py-200 > div')

# creata muaban folder
divMuaBanCryptoName = divMuaBanCrypto.text
if not os.path.exists(f'./dataCoin98/Learn/{divMuaBanCryptoName}'):
    os.mkdir(f'./dataCoin98/Learn/{divMuaBanCryptoName}')

subdivMuaBanCrypto = driver.find_elements(
    By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div')

print('aaa')
for i in range(len(subdivMuaBanCrypto)):
    driver.find_element(
        By.CSS_SELECTOR, f'#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child({i+1}) >  div').click()
    time.sleep(2)
    articles = driver.find_elements(
        By.CSS_SELECTOR, '#channel-body > div.max-w-w1440.w-full.mx-auto.relative.pt-sp200.md\:pt-1600.lg\:pt-1000.flex > div.w-full.lg\:w-\[calc\(100\%-320px\)\].pl-0.flex.justify-center.lg\:ml-auto > div > div.flex.flex-col.mx-auto.w-full.max-w-w728 > div')
    time.sleep(1)
    print(len(articles))
    if (i == 0):
        driver.find_element(
            By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div > button').click()
        time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    # driver.find_element(
    #     By.CSS_SELECTOR, f'#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child({i+1}) > div').click()
    # time.sleep(2)
    # driver.find_element(
    #     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
    # time.sleep(2)
    # print(clickButton.get_attribute("outerHTML"))
    break
    pass

# driver.quit()
# sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered
# sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered
# sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered
# sidebar-portal > div.grow > div:nth-child(5) > div > button
