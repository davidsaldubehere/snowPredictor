from guy import Guy
import lxml.html
from lxml.cssselect import CSSSelector
import urllib.request
import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context
#preload files for smoother loading
externalJS = f"<script>{open('app.js', 'r').read()}</script>"
externalCSS = f"<style>{open('style.css', 'r').read()}</style>"
class Simple(Guy):
    #parse js and css
    __doc__=f"{externalJS}{externalCSS}{open('index.html', 'r').read()}"
    agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    baseURL = "https://www.accuweather.com"
    async def reset(self):
        await self.js.recieve("Location Saved: click load snow day prediction", "results")
        await self.js.recieve("Location has been saved", 'locations')
        await self.js.recieve("Click load snow day prediction above", 'snowfall')
    def splitURL(self, response, string1, string2):
        split = response.split(string1)
        split.insert(1, string2)
        return "".join(split)

    async def getSnowAmount(self):
        r1 = urllib.request.Request(f"{self.baseURL}{open('locationKeys.txt', 'r').read()}", None, self.agent)
        response = urllib.request.urlopen(r1).url
        finalURL = self.splitURL(response, "weather-forecast", "winter-weather-forecast")
        r1 = urllib.request.Request(finalURL, None, self.agent)
        response = urllib.request.urlopen(r1).read()
        doc = lxml.html.fromstring(response)
        if len(doc.xpath('//div[@class="phrase"]'))>4:
            snow = ''.join(doc.xpath('//div[@class="phrase"]')[0].itertext()).replace("\t", "")
        else:
            snow = 'No snow predicted'
        return snow
    async def getSnowPrediction(self):
        await self.js.setLoader()
        r1 = urllib.request.Request(f"{self.baseURL}{open('locationKeys.txt', 'r').read()}", None, self.agent)
        response = urllib.request.urlopen(r1).url
        finalURL = self.splitURL(response, "weather-forecast", "snow-day-weather")
        r1 = urllib.request.Request(finalURL, None, self.agent)
        response = urllib.request.urlopen(r1).read()
        doc = lxml.html.fromstring(response)
        today = ''.join(doc.xpath('//div[@class="cond"]')[0].itertext()).replace("\t", "")
        tomorrow = ''.join(doc.xpath('//div[@class="cond"]')[1].itertext()).replace("\t", "")
        timeObject = datetime.datetime.today()
        month = timeObject.month
        day = timeObject.day
        snowText = await self.getSnowAmount()
        await self.js.setLoader()
        await self.js.recieve(snowText, 'snowfall')
        await self.js.recievePrediction(str(month) + '/' + str(day) + today, str(month) + '/' + str(day+1) + tomorrow)
    async def clear(self):
        open("locationKeys.txt", "w").write('')
        await self.js.recieve("Location cleared", 'locations')

    async def check(self):
        if(open("locationKeys.txt", "r").read()!=""):
            await self.reset()
    async def saveFile(self, value):
        testFile = open("locationKeys.txt", "w")
        testFile.write(value)
        testFile.close()
        await self.reset()
    
    async def getLocations(self, search):
        await self.js.setLoader()
        r1 = urllib.request.Request(f"{self.baseURL}/en/search-locations?query={search.replace(' ', '+')}", None, headers=self.agent)
        await self.js.recieve("searching", "locations")
        response = (urllib.request.urlopen(r1).read())
        await self.js.recieve("processing", "locations")
        doc = lxml.html.fromstring(response)
        selAnchor = CSSSelector('a')
        foundElements = selAnchor(doc)
        found = [e for e in foundElements if "three" in str(e.get("href"))]
        found.pop(0)
        text = [e.text_content().replace("\t", "").replace("\n", "") for e in found]
        links = [e.get("href") for e in found]
        await self.js.recieveSearch(text, links)
        await self.js.setLoader()

if __name__ == "__main__":
    x=Simple()
    x.serve()