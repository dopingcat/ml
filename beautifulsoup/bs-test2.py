from bs4 import BeautifulSoup

html = """
	<html><body>
		<ul>
			<li><a href="http://www.google.com">google</a></li>
			<li><a href="http://www.facebook.com">facebook</a></li>
		</ul>
	</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links:
	href = a.attrs['href']
	text = a.string
	print(text, ">", href)