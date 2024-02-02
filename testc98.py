import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}
r = requests.get(
    'https://coin98.net/thanh-khoan-tap-trung-clmm-la-gi', headers=headers)

with open('testc98.html', 'w', encoding='utf8') as file:
    file.write(r.text)
