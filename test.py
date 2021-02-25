import requests
import lxml.html

agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
search = input("Enter locations")
response = requests.get(f"https://www.accuweather.com/en/search-locations?query={search}", headers=agent).text
doc = lxml.html.document_fromstring(response)
test = (doc.xpath("//div[@class='results-container']"))
print(lxml.html.tostring(test[0]))