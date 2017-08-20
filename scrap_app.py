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

from bs4 import BeautifulSoup
import urllib.request as req

# Set URL
baseUrl = "https://play.google.com"
searchUrl = baseUrl + "/store/search?q=%ED%95%98%EB%82%98%EC%9D%80%ED%96%89&c=apps"   # /store/search?q=검색어&c=apps

# Get AppStore Page
res = req.urlopen(searchUrl)

searchSoup = BeautifulSoup(res, "html.parser")
appList = searchSoup.select("div.id-card-list > div.card > div.card-content")

# print(appList)

# for a in searchSoup.find_all('a', href=True):
#     print("Found the URL:", a['href'])

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
            print(data.find('div', {'class': 'title'}).text, ' : ', data.find('', {'class': 'content'}).text)


    print()