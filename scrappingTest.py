import requests
from bs4 import BeautifulSoup

rank_url = "http://section.cafe.naver.com/CafeRankingList.nhn"
response = requests.get(rank_url)

bs = BeautifulSoup(response.text, 'html.parser')
results = bs.select("tbody > tr > td > div > a")
for result in results :
    print (result.text.strip())