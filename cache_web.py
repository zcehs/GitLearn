import requests as rq
import json
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
print(soup.prettify()) # 把排版後的 html 印出來

titles = []

for title in soup.select(".title"):
    if title.a:
        titles.append(title.a.text)

with open("NBA_titles.json", "w", encoding="utf-8") as f:
    json.dump(titles, f, indent=2, ensure_ascii=False)