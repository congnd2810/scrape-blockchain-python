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

listFodlers = glob.glob('./data/*')

for folder in listFodlers:
    folderName = folder.split('/')[-1]
    if not os.path.exists(f'./dataHtml/{folderName}'):
        os.mkdir(f'./dataHtml/{folderName}')
    for file in glob.glob(f'{folder}/*'):
        fileName = file.split('/')[-1].replace('.json', '')
        if not os.path.exists(f'./dataHtml/{folderName}/{fileName}'):
            os.mkdir(f'./dataHtml/{folderName}/{fileName}')
        f = open(file, 'r', encoding='utf-8')
        urls = json.loads(f.read())
        for url in urls['articles']:
            urlname = url.split('/')[-1]
            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(chrome_options)
            # print(url)
            try:
                driver.get(url)
                time.sleep(2)
                content = driver.find_element(
                    By.CSS_SELECTOR, "#post-content-colCenter")
                htmlContent = content.get_attribute('outerHTML')

                with open(f"./dataHtml/{folderName}/{fileName}/{urlname}.html", "w", encoding="utf-8") as file:
                    file.write(htmlContent)
                driver.quit()
            except:
                print(f'error {url} from {file} and {folder}')            
        print(f'done {fileName}')
    print(f'done {folderName}')
