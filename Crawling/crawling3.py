
import requests
from bs4 import BeautifulSoup

url = "http://test.linuxmaster.net/3.html"
htmlData = requests.get(url)
bs_obj = BeautifulSoup(htmlData.text, "html.parser") # BeautifulSoup Class를 사용해서 완벽히 html로 정제함

print(bs_obj.find("li"))
print(bs_obj.findAll("li"))

li = bs_obj.findAll("li")
print(type(li))
for i in li:
    if "꼬깔콘" in i:
        print(i)