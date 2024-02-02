import requests
import json

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


# result = res.json()
# fjson = open(f'./dataCoin98/Learn/MuaBanCrypto/MuaBan.json',
#              'w', encoding='utf-8')

# jsonQ = json.dumps(result, indent=2)

url = "https://insights.coin98.com/adapters/portal/user/search"

payload = json.dumps({
    "orgID": "615d4bee576bf9edd0d07009",
    "page": 1,
    "size": 10,
    "isAlpha": True,
    "lang": "vn",
    "listIdSubCate": [
        "651fad6f7448dc9f106b902e"
    ],
    "sort": "-time"
})
headers = {
    'Content-Type': 'application/json',
    'Cookie': '__cf_bm=iYEQ1q24UxZiTE5EX1w8NDgsiJGP_c.ORiJ8NK4X.sY-1704968049-1-Ad4RJeSVn1Z09XCW68B5S9QYCrIO+EMAWHqbBo4JYaHyDz6gY+qDkKFMIYwfXE9Pd6a0+aggU2VNo2L5SJ6+Hak=',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImQ1MjBjN2E4LTQyMWItNDU2My1iOTU1LWY1YWJjNTZiOTdlYyIsInRva2VuIjoiIiwiaWF0IjoxNjk3NjE0NTgxLCJleHAiOjIwMTI5NzQ1ODF9.b5h9RIk7z8BVJGVjpxnvQ1CKpQ8ish2nJmK9DXhUhw0',
    'Locale': 'en',
    'Os': 'website',
    'Osversion': 'website'

}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
# fjson.write(jsonQ)
