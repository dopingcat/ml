from bs4 import BeautifulSoup
import urllib.request
import time

url = "http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105"
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
results = soup.select("#section_body a")
for result in results:
	print("Title : ", result.attrs["title"])
	url_article = result.attrs["href"]
	res = urllib.request.urlopen(url_article)
	soup_article = BeautifulSoup(res, "html.parser")
	content = soup_article.select_one("#articleBodyContents")

	output = ""
	for item in content.contents:
		stripped = str(item).strip()
		if stripped == "":
			continue
		if stripped[0] not in ["<", "/"]:
			output += str(item).strip()
			
	print(output.replace("본문 내용TV플레이어", ""))
	print("")
		
	# 요청 부하 방지용 sleep
	time.sleep(1)