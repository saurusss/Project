import requests
from bs4 import BeautifulSoup
 
url = "http://finance.naver.com/item/main.nhn?code=035420"
html = requests.get(url).text
 
# soup = BeautifulSoup(html, "html5lib")
soup = BeautifulSoup(html, "html.parser")
tags = soup.select("#_market_sum")
cap = tags[0].parent.text
cap = cap.replace('\t', '')
cap = cap.replace('\n', '')
cap = cap.strip()
print(cap)