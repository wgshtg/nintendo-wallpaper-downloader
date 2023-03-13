# Nintendo Birthday Wallpaper Downloader

- 2021 wallpaper URL: <https://www.nintendo.co.jp/wallpaper/21_HBD_A/index.html>
- 2022 wallpaper URL: <https://www.nintendo.co.jp/wallpaper/22_HBD_A/index.html>

## Environment

[python3](https://www.python.org/)

## Execution

```sh
pip3 install requests BeautifulSoup4

# Default download 2022 wallpapers
# If you want to download 2021 wallpapers, you have to change WALLPAPER_PATH to 21_HBD_A
python3 scrapy.py
```

## Result

```stdout
img
├── 22_HBD_Animal_1080_1920.jpg
├── 22_HBD_Animal_1200_1920.jpg
├── 22_HBD_Animal_1242_2688.jpg
├── 22_HBD_Animal_1536_2048.jpg
├── 22_HBD_Animal_1920_1080.jpg
.......
```
