import requests
from bs4 import BeautifulSoup

url = "http://test.linuxmaster.net/2.html"
htmlData = requests.get(url)
# print(htmlData.text)

bs_obj = BeautifulSoup(htmlData.text, 'html.parser')
print(bs_obj.text)

# find() 함수를 이용해서 div 태그를 찾는다.
# 실행 결과
#<div>포카칩</div>

#print(bs_obj.find("div"))

#div = bs_obj.find("div") # <div>포카칩</div>
#print(div.text) # <div> 태그 안에 데이터 포카칩

print(bs_obj.find("div").text)   # 포카칩
print(bs_obj.find("title").text) # ::: 크롤링 테스트 웹페이지 :::