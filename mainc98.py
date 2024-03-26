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

weburl = 'https://coin98.net/'

seriesThePortfolio = 'https://coin98.net/series/the-portfolio-o9j1ura7'
seriesTheSpotlight = 'https://coin98.net/series/the-spotlight-9jc8e340'
seriesTheTruth = 'https://coin98.net/series/the-truth-0zwmyto6'
seriesTheModel = 'https://coin98.net/series/the-model-ymf87gux'

report = 'https://coin98.net/report'
inside_coin98 = 'https://coin98.net/inside-coin98'


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options)
driver.set_page_load_timeout(10)

driver.get(trading)


def requests_complete(driver):
    return driver.execute_script("return (window.performance.getEntriesByType('resource') || []).filter(r => !r.responseEnd).length === 0;")


listUrlArticales = []

time.sleep(2)
# articles = driver.find_elements(
#     By.CSS_SELECTOR, "#layout-normal-minHeight > main > div > div.style_contentSeries__2YVxe > div > div.style_posts__KmXDx > div > div.style_posts__8cqkq > div")
articles = driver.find_elements(
    By.CSS_SELECTOR, "#channel-body > div.max-w-w1440.w-full.mx-auto.relative.pt-sp200.md\:pt-1600.lg\:pt-1000.flex > div.w-full.lg\:w-\[calc\(100\%-320px\)\].pl-0.flex.justify-center.lg\:ml-auto > div > div.flex.flex-col.mx-auto.w-full.max-w-w728 > div")

# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
#            "#layout-normal-minHeight > main > div > div.style_contentSeries__2YVxe > div > div.style_posts__KmXDx > div > div.style_posts__8cqkq")))
newArticles = []
reportArticles = []
articlesLength = 0
count = 0

while True:

    '''lấy bài c98 các mục có option tích
    div_element_to_scroll = driver.find_element(
        By.CSS_SELECTOR, '#layout-normal-minHeight > main > div > div.style_contentWrapper__ixUnP.style_isCoin98__TqZ_W.style_content__TK5yo')
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", div_element_to_scroll)
    time.sleep(2)
    newArticles = driver.find_elements(
        By.CSS_SELECTOR, "#layout-normal-minHeight > main > div > div.style_contentWrapper__ixUnP.style_isCoin98__TqZ_W.style_content__TK5yo > div.style_resultWrapper__jFum7 > div > div.style_posts__b_3E_.style_more__c_weN > div")

    if len(newArticles) > articlesLength:
        articlesLength = len(newArticles)
        count += 1
    else:
        break
    '''
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    newArticles = driver.find_elements(
        By.CSS_SELECTOR, "#channel-body > div.max-w-w1440.w-full.mx-auto.relative.pt-sp200.md\:pt-1600.lg\:pt-1000.flex > div.w-full.lg\:w-\[calc\(100\%-320px\)\].pl-0.flex.justify-center.lg\:ml-auto > div > div.flex.flex-col.mx-auto.w-full.max-w-w728 > div")
    print(len(newArticles))
    if len(newArticles) > articlesLength:
        articlesLength = len(newArticles)
        count += 1
    else:
        break
    '''get report and inside coin98'''
    # reportArticles = driver.find_elements(
    #     By.CSS_SELECTOR, "#layout-normal-minHeight > main > div:nth-child(3) > div > div.style_customRow__l_Y1O.row > div")
    # if len(reportArticles) > articlesLength:
    #     articlesLength = len(reportArticles)
    #     count += 1
    # else:
    # break
    '''*****'''
    '''get series'''
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
    # articles = driver.find_elements(
    #     By.CSS_SELECTOR, '#channel-body > div > div.flex.items-start.flex-col.lg\:flex-row > div.grow.lg\:ml-1500.lg\:mt-500 > div > a')
    # if len(articles) > articlesLength:
    #     articlesLength = len(articles)
    #     count += 1
    # else:
    #     break
    '''***'''
    # click button xem thêm
    # try:
    #     button = driver.find_element(
    #         By.CSS_SELECTOR, '#layout-normal-minHeight > main > div > div.style_contentSeries__2YVxe > div > div.style_posts__KmXDx > div > div.style_buttonWrapper__KYxkd > button')
    #     button.click()
    # except:
    #     pass

# for a in reportArticles:
#     urlArticle = a.find_element(By.CSS_SELECTOR, "div a")
#     newUrl = urlArticle.get_attribute('href')
#     print(newUrl)
#     listUrlArticales.append(newUrl)


# for a in articles:
#     urlArticle = a.find_element(By.CSS_SELECTOR, "div a")
#     newUrl = urlArticle.get_attribute('href')
#     listUrlArticales.append(newUrl)

for a in articles:
    urlArticle = a.find_element(By.CSS_SELECTOR, "a")
    newUrl = a.get_attribute('href')
    listUrlArticales.append(newUrl)

print(listUrlArticales)
tintucbtc = {'articles': listUrlArticales}

fjson = open(f'./dataCoin98/Learn/Trading/Trading.json',
             'w', encoding='utf-8')

jsonQ = json.dumps(tintucbtc, indent=2)

fjson.write(jsonQ)

driver.quit()
