"""
파일명 : crawling5.py
프로그램 설명 : 네이버 페이지에서 네이버를 시작페이지로 추출하기
"""

import requests
from bs4 import BeautifulSoup

# 네이버를 시작페이지로 추출하기
url = "https://www.naver.com/"
htmlData = requests.get(url)
bs_obj = BeautifulSoup(htmlData.text, "html.parser")
print(bs_obj)