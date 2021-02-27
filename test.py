import requests
import lxml.html
from lxml.cssselect import CSSSelector
import urllib.request
import datetime
agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
r1 = urllib.request.Request(f"https://www.accuweather.com/web-api/three-day-redirect?key=2522881&target=", None, agent)
response = urllib.request.urlopen(r1).url
splitURL = response.split("weather-forecast")
splitURL.insert(1,"snow-day-weather")
finalURL = "".join(splitURL)
r1 = urllib.request.Request(finalURL, None, agent)
response = urllib.request.urlopen(r1).read()
doc = lxml.html.fromstring(response)
today = ''.join(doc.xpath('//div[@class="cond"]')[0].itertext()).replace("\t", "")
tomorrow = ''.join(doc.xpath('//div[@class="cond"]')[1].itertext()).replace("\t", "")
print(today)
print(tomorrow)
print(str(datetime.datetime.today().month) + str(datetime.datetime.today().day))