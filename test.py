import requests
import lxml.html
from lxml.cssselect import CSSSelector
import urllib.request
agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
search = input("Enter locations")
r1 = urllib.request.Request(f"https://www.accuweather.com/", None, agent)
response = (urllib.request.urlopen(r1).read())
doc = lxml.html.fromstring(response)
selAnchor = CSSSelector('a')
foundElements = selAnchor(doc)
found = [e for e in foundElements if "three" in str(e.get("href"))]
text = [e.text_content().replace("\t", "").replace("\n", "") for e in found]
links = [e.get("href") for e in found]
print(links)