# Nintendo Birthday Wallpaper Downloader

## 環境準備

[python3](https://www.python.org/)

## 執行步驟

```sh
# 第一步：安裝套件
pip3 install requests BeautifulSoup4

# 第二步：執行腳本
python3 scrapy.py
```

## 執行畫面

### 正常執行

請選擇要下載哪個年度壁紙？

1. 2022 年
2. 2023 年
輸入選項編號 2
開始下載 2023 年度壁紙...

### 錯誤執行

請選擇要下載哪個年度壁紙？

1. 2022 年
2. 2023 年
輸入選項編號 3
3 不是有效選項編號，請輸入有效選項編號！

## 正常執行結果

```stdout
images
├── 22_HBD_Animal_1080_1920.jpg
├── 22_HBD_Animal_1200_1920.jpg
├── 22_HBD_Animal_1242_2688.jpg
├── 22_HBD_Animal_1536_2048.jpg
├── 22_HBD_Animal_1920_1080.jpg
.......
```
