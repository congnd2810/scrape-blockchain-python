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

weburl = 'https://coin98.net/'

seriesThePortfolio = 'https://coin98.net/series/the-portfolio'
seriesTheSpotlight = 'https://coin98.net/series/the-spotlight'
seriesTheTruth = 'https://coin98.net/series/the-truth'

cryptoForNewUser = 'https://coin98.net/learn/detail?subCategory=651fabddc5862d9fdb972752'
muabancrypto_muaban = 'https://coin98.net/learn/detail?subCategory=651facbc98bcd69fb10b12d7'
muabancrypto_luutru = 'https://coin98.net/learn/detail?subCategory=651fad6f7448dc9f106b902e'
muabancrypto_baomat = 'https://coin98.net/learn/detail?subCategory=651fad9a167fbb9f9515155c'
muabancrypto_huongdanchuyencoin = 'https://coin98.net/learn/detail?subCategory=65961b1c8c14e12b0c06f497'

blockchainAndDefi_blockchain = 'https://coin98.net/learn/detail?subCategory=651fadedb37b429ec18a7dae'
blockchainAndDefi_defi = 'https://coin98.net/learn/detail?subCategory=651fae1dbd63d49f48c00b51'
blockchainAndDefi_hesinhthai = 'https://coin98.net/learn/detail?subCategory=6593c4038e35d62acc3754f1'
blockchainAndDefi_amm = 'https://coin98.net/learn/detail?subCategory=6596218fd1987e2ae19c9dbf'
blockchainAndDefi_identity = 'https://coin98.net/learn/detail?subCategory=656ee48cc28ae2b9565bce64'
blockchainAndDefi_stablecoin = 'https://coin98.net/learn/detail?subCategory=65962a11027d8b2af62231f8'
blockchainAndDefi_nft_gaming_metaverse = 'https://coin98.net/learn/detail?subCategory=65962abca9ff982ac57edce1'
blockchainAndDefi_quydautu = 'https://coin98.net/learn/detail?subCategory=65964bf5da5b982ae8ba67b9'
blockchainAndDefi_luadao = 'https://coin98.net/learn/detail?subCategory=658b9c65a9ff982ac5742c2f'
blockchainAndDefi_options = 'https://coin98.net/learn/detail?subCategory=65964caf1a6ecc2abe7a9b57'

congcu = 'https://coin98.net/learn/detail?subCategory=651faeccf1329b9ed8b02e1d'

trading = 'https://coin98.net/learn/detail?subCategory=651fb1987b391d9faa23318c'

report = 'https://coin98.net/menu/report'
inside_coin98 = 'https://coin98.net/menu/inside-coin98'

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
