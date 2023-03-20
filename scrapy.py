import os
import sys
import threading
import requests
from bs4 import BeautifulSoup

print("請選擇要下載哪個年度壁紙？")
print("1. 2022 年")
print("2. 2023 年")

select = input("輸入選項編號")

WALLPAPER_YEAR_PATH = ''
if select == "1":
    WALLPAPER_YEAR_PATH = '22_HBD_A'
elif select == "2":
    WALLPAPER_YEAR_PATH = '23_HBD_A'
else:
    print(f"{select} 不是有效選項編號，請輸入有效選項編號！")
    sys.exit()

baseUrl = 'https://www.nintendo.co.jp/wallpaper'
url = baseUrl + f'/{WALLPAPER_YEAR_PATH}/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

topicLinks = []
wallpaperLinks = []
wallpaperNames = []
WALLPAPER_FOLDER = 'images'

# 抓出所有主題頁面
for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x}):
    # /22_HBD_Mario/index.html
    topicHref = link.get('href').lstrip('..')
    # https://www.nintendo.co.jp/wallpaper/22_HBD_Mario/index.html
    topicLink = baseUrl + topicHref
    topicLinks.append(topicLink)

# 抓出所有壁紙連結和下載
for topicLink in topicLinks:
    response = requests.get(topicLink)
    soup = BeautifulSoup(response.text, 'html.parser')
    # https://www.nintendo.co.jp/wallpaper/22_HBD_Mario
    baseUrl = topicLink.rstrip('/index.html')
    for link in soup.find_all('a', attrs={'href': lambda x: x and 'HBD' in x and not '..' in x}):
        # img/22_HBD_Zelda_1080_1920.jpg
        imgHref = link.get('href')
        imgName = imgHref.lstrip('img/')
        # https://www.nintendo.co.jp/wallpaper/22_HBD_Mario/img/22_HBD_Mario_1242_2688.jpg
        imgLink = baseUrl + '/' + imgHref
        wallpaperLinks.append(imgLink)
        wallpaperNames.append(imgName)

# 建立壁紙資料夾
os.makedirs(WALLPAPER_FOLDER, exist_ok=True)


# 下載壁紙
def download(url, filename):
    response = requests.get(url)
    path = os.path.join(WALLPAPER_FOLDER, filename)
    with open(path, 'wb') as f:
        f.write(response.content)


# 使用多線程來進行並行下載
threads = []
for link, name in zip(wallpaperLinks, wallpaperNames):
    thread = threading.Thread(target=download, args=(link, name))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
