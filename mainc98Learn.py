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
    By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div > div')

# for i in range(len(subdivMuaBanCrypto)):
#     divName = subdivMuaBanCrypto[i]
#     driver.find_element(
#         By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
#     time.sleep(2)
#     driver.find_element(
#         By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
#     time.sleep(2)
#     # driver.find_element(
#     #     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div > button').click()
#     # time.sleep(2)
#     print(divName)
#     # div.find_element(By.CSS_SELECTOR, 'div').click()

#     # print(clickButton.get_attribute("outerHTML"))
#     pass
# '''## tích mục mua bán'''
driver.find_element(
    By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered').click()
time.sleep(2)
# handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Mua bán.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục lưu trữ'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Lưu trữ.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục bảo mật'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(3) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Bảo mật.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(3) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Hướng dẫn chuyển coin'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(4) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Hướng dẫn chuyển coin.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(4) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Hướng dẫn thêm mạng'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(5) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Hướng dẫn thêm mạng.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(5) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Đầu tư crypto'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(6) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Mua bán Crypto/Đầu tư Crypto.json')
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(5) > div.px-500.transform.opacity-100 > div:nth-child(6) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)


# '''# dropdown Blockchain & Defi'''
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div > button').click()
# WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
#                                                                     '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear')))
# '''## tích mục Blockchain'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Blockchain.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(1) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Defi'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Blockchain.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(2) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Hệ sinh thái'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(3) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Hệ sinh thái.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(3) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục AMM'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(4) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/AMM.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(4) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Lending'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(5) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Lending.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(5) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục StableCoin'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(6) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/StableCoin.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(6) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Options'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(7) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Options.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(7) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục NFT & Gaming & Metaverse'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(8) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/NFTGamingMetaverse.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(8) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục SocialFi'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(9) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/SicialFi.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(9) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục VCs'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(10) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/VCs.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(10) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục Scam'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(13) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Scam.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(13) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# '''## tích mục SocialFi'''
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(12) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# # handleToJson(driver, './dataCoin98/Learn/Blockchain & DeFi/Other.json')
# driver.find_element(By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div.px-500.transform.opacity-100 > div:nth-child(12) > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)
# sidebar-portal > div.grow > div:nth-child(5) > div.flex.justify-between.text-text-primary.md\:hover\:cursor-pointer.items-center.px-300.py-200 > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear
# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered > div').click()
# time.sleep(2)

# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(6) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(7) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered > div').click()
# time.sleep(2)

# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(7) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(8) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear.bg-toggle-background.group-hover\/toggleCheck\:bg-toggle-background-hovered > div').click()
# time.sleep(2)

# driver.find_element(
#     By.CSS_SELECTOR, '#sidebar-portal > div.grow > div:nth-child(8) > div > div > div.flex.items-center.h-300.w-300.rounded-075.p-025.transition-all.duration-200.ease-linear').click()
# time.sleep(2)

# driver.quit()
