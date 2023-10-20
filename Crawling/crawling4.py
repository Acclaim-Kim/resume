"""
파일명 : crawling4.py
프로그램 설명 : find()를 이용해서 class 찾기
"""

import requests
from bs4 import BeautifulSoup

url = "http://test.linuxmaster.net/4.html"
htmlData = requests.get(url)
bs_obj = BeautifulSoup(htmlData.text, "html.parser")

ul = bs_obj.find("ul", {"class" : "greet"})
print(ul)