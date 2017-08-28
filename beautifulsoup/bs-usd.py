from bs4 import BeautifulSoup
import urllib.request as req

# GET HTML
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

# Analysis HTML
soup = BeautifulSoup(res, "html.parser")

price = soup.select("div.head_info > span.value")
# print("USD/KRW : ", price)

for p in price:
	print(p.text)
