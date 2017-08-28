# Required
# 1. BeautifulSoup4
#       pip install beautifulsoup4
# 2. Selenium
#       pip install selenium
# 3. PhantomJS
#       apt-get install -y wget libfontconfig
#       mkdir -p /home/root/src && cd $_
#       wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
#       tar jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
#       cd phantomjs-2.1.1-linux-x86_64/bin/
#       cp phantomjs /usr/local/bin/
# 4. Korean Font
#       apt-get install -y fonts-nanum*

import os
import sys
import datetime
import urllib.request as req
import urllib.parse as parse
from bs4 import BeautifulSoup

# Prepare directory
now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

if not os.path.exists(nowDate):
    os.mkdir(nowDate)


# Set URL
baseUrl = "https://play.google.com"
searchUrl = "/store/search?"

# The URL is defined as follows
# https://play.google.com/store/search?q=검색어&c=apps
if len(sys.argv) <= 1:
    targetUrl = baseUrl + searchUrl + "q=%ED%95%98%EB%82%98%EC%9D%80%ED%96%89&c=apps"
    print("[알림] 매개 변수 미입력 시 기본 검색어는 '하나은행' 입니다.")
    print("[System] TargetUrl : ", targetUrl)
else:
    input = sys.argv[1]
    params = {'q': input}
    encodedText = parse.urlencode(params)
    targetUrl = baseUrl + searchUrl + encodedText + "&c=apps"
    print("[System] TargetUrl : ", targetUrl)


# TO-DO : nowDate를 폴더명으로 해당날짜의 스크린샷 저장

# Get AppStore Page
res = req.urlopen(targetUrl)

searchSoup = BeautifulSoup(res, "html.parser")
appList = searchSoup.select("div.id-card-list > div.card > div.card-content")

for app in appList:
    print("Title : ", app.select_one("div.details > a.title")["title"])
    appUrl = app.select_one("a")["href"]

    res = req.urlopen(baseUrl + appUrl)
    detailSoup = BeautifulSoup(res, "html.parser")
    details = detailSoup.select("div.details-section.metadata")
    # print("Detail Info : ", details)
 
    for info in details:
        metaData = info.select("div.meta-info")
        for data in metaData:
            print(data.find('div', {'class': 'title'}).text, ':', data.find('', {'class': 'content'}).text)


    print()