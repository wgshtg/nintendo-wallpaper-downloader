import requests
from bs4 import BeautifulSoup

# 總覽頁面
portalUrl = 'https://www.nintendo.co.jp/wallpaper/22_HBD_A/index.html'
response = requests.get(portalUrl)
soup = BeautifulSoup(response.text, 'html.parser')

categoryPages = []

# 取得每個分類頁面
for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x and '..' in x}):
    item_href = link.get('href').lstrip('../')
    baseUrl = portalUrl.rstrip('22_HBD_A/indext.html')
    pageUrl = baseUrl + '/' + item_href
    print(pageUrl)
    categoryPages.append(pageUrl)

# 分類頁面上圖片下載連結
for page in categoryPages:
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x and not '..' in x}):
        img_href = link.get('href')
        baseUrl = page.rstrip('index.html')
        downloadUrl = baseUrl + img_href
        print(downloadUrl)
        response = requests.get(downloadUrl)
        with open(img_href, 'wb') as f:
            f.write(response.content)
