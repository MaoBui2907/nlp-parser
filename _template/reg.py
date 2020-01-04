import urllib.request
from bs4 import BeautifulSoup
import re

response = urllib.request.urlopen("https://vnexpress.net/the-gioi/trump-ky-luat-ve-hong-kong-4018779.html")
html = response.read()
content = html.decode("utf8")

regex = r"<article class=\"content_detail(.|\n)*?</article>"

search = re.search(regex, content)

news = content[search.start():search.end()]
soup = BeautifulSoup(news,"html.parser")
ret = soup.get_text(strip=True)

f = open("output.txt", "w",encoding="utf8")
f.write(ret)
f.close()

regname = r"[A-Z][^\s\.,\(\)\"]*(\s[A-Z][^\s\.,\(\)\"]*)*"
names = re.finditer(regname, ret)
for name in names:
	print(ret[name.start():name.end()])

regdate = r"[0-9]+(/[0-9]+)+"	
dates = re.finditer(regdate, ret)
for date in dates:
	print(ret[date.start():date.end()])
