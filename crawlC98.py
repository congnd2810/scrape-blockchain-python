import requests
import glob
import json
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

listFodlers = glob.glob('./dataCoin98/*')

for folder in listFodlers:
    folderName = folder.split('\\')[-1]
    if not os.path.exists(f'./dataHtmlCoin98/{folderName}'):
        os.mkdir(f'./dataHtmlCoin98/{folderName}')
    if folder == './dataCoin98\\Learn':
        for subFolder in glob.glob(f'{folder}/*'):
            subFolderName = subFolder.split('\\')[-1]
            if not os.path.exists(f'./dataHtmlCoin98/{folderName}/{subFolderName}'):
                os.mkdir(f'./dataHtmlCoin98/{folderName}/{subFolderName}')
            for file in glob.glob(f'{subFolder}/*'):
                filename = file.split('\\')[-1]
                f = open(file, 'r', encoding='utf-8')
                urls = json.loads(f.read())
                for url in urls['articels']:
                    chrome_options = Options()
                    chrome_options.add_experimental_option("detach", True)
                    driver = webdriver.Chrome(chrome_options)
                    try:
                        urlname = url.split('/')[-1]
                        driver.get(url)
                        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "#post-detail > div.flex.pt-300.flex-col.justify-center.w-full.max-w-w1280.mx-auto.pb-800")))
                        content1 = driver.find_element(
                            By.CSS_SELECTOR, "#post-detail > div.flex.pt-300.flex-col.justify-center.w-full.max-w-w1280.mx-auto.pb-800")
                        content2 = driver.find_element(
                            By.CSS_SELECTOR, "#detail-content")
                        # post-detail > div.flex.pt-300.flex-col.justify-center.w-full.max-w-w1280.mx-auto.pb-800
                        # detail-content
                        # post-detail > div.flex.pt-300.flex-col.justify-center.w-full.max-w-w1280.mx-auto.pb-800
                        htmlContent1 = content1.get_attribute('outerHTML')
                        htmlContent2 = content2.get_attribute('outerHTML')

                        with open(f"./dataHtmlCoin98/{folderName}/{subFolderName}/{urlname}.html", "w", encoding="utf-8") as f:
                            f.write(htmlContent1)
                            f.write(htmlContent2)
                            f.close()
                        driver.quit()
                        time.sleep(1)
                    except Exception as e:
                        print(e)
                        print(f'error {url} from {filename} and {folderName}')
        pass
    else:
        # for file in glob.glob(f'{folder}/*'):
        #     if not os.path.exists(f'./dataHtmlCoin98/{folderName}'):
        #         os.mkdir(f'./dataHtmlCoin98/{folderName}')
        #     f = open(file, 'r', encoding='utf-8')
        #     urls = json.loads(f.read())
        pass
