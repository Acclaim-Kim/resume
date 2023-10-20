"""
파일명 : crawling1.py
프로그램 설명 : urlopen(), BeautifulSoup() 사용하기
BeautifulSoup 은 통신 기능은 가지고 있지 않으므로 통신 기능이 있는 urllib.request 를 함께 사용해야 한다.
참고 : https://cafe.naver.com/linuxmasternet/287
"""

import urllib.request
import bs4

url = "http://test.linuxmaster.net/"

# 소켓으로 연결해서 html 데이터를 가져온다.
htmlData = urllib.request.urlopen(url)
# print(htmlData.read())
bs_obj = bs4.BeautifulSoup(htmlData, "html.parser")
print(bs_obj)


