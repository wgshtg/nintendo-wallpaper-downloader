import requests
from bs4 import BeautifulSoup
import threading
import os

# 總覽頁面網址
# 22_HBD_A, 21_HBD_A
WALLPAPAER_PATH = '21_HBD_A'
portalUrl = f'https://www.nintendo.co.jp/wallpaper/{WALLPAPAER_PATH}/index.html'
response = requests.get(portalUrl)
soup = BeautifulSoup(response.text, 'html.parser')

categoryPages = []

# 取得每個分類頁面網址
for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x and '..' in x}):
    item_href = link.get('href').lstrip('../')
    baseUrl = portalUrl.rstrip(f'{WALLPAPAER_PATH}/indext.html')
    pageUrl = baseUrl + '/' + item_href
    categoryPages.append(pageUrl)

# 存放圖片下載網址和檔案名稱
imgUrls = []
imgNames = []

# 分類頁面上圖片下載網址
for page in categoryPages:
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x and not '..' in x}):
        img_href = link.get('href')
        imgNames.append(img_href)
        baseUrl = page.rstrip('index.html')
        downloadUrl = baseUrl + img_href
        imgUrls.append(downloadUrl)


def download(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)


# 確保 img 資料夾存在
os.makedirs('img', exist_ok=True)

# 使用多線程來進行並行下載
threads = []
for url, filename in zip(imgUrls, imgNames):
    thread = threading.Thread(target=download, args=(url, filename))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
