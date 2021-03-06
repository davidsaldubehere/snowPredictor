from guy import Guy
import lxml.html
from lxml.cssselect import CSSSelector
import urllib.request
import ssl
import datetime
ssl._create_default_https_context = ssl._create_unverified_context
class Simple(Guy):
    __doc__="""
    <head>
    <script src="https://kit.fontawesome.com/39f2a6897b.js" crossorigin="anonymous"></script>
    </head>
    <script>
    setTimeout(function(){self.check() }, 500);
    var els = [];
    var glinks;
    var loader = true;
    function recieve(value, target){
        document.getElementById(target).innerHTML = value;
        
    }
    function recievePrediction(today, tomorrow){
        document.getElementById('results').innerHTML='';
        let td = document.createElement("H2");
        td.innerHTML='Today: ' + today;
        let tm = document.createElement("H2");
        tm.innerHTML = 'Tomorrow: ' + tomorrow;
        document.getElementById('results').appendChild(td);
        document.getElementById('results').appendChild(tm);
    }
    function recieveSearch(values, links){
        els = [];
        for(var i=0; i<values.length;i++){
            var li = document.createElement("LI");
            var btn = document.createElement("A");
            els.push(btn)
            glinks = links;
            btn.innerHTML = values[i];
            li.appendChild(btn);
            document.getElementById("results").appendChild(li);
        }
        for(let a = 0; a<els.length;a++){
            els[a].addEventListener("click", function(){
                self.saveFile(glinks[a]);
            });
        }
    }
    function openNav() {
        document.getElementById("mySidenav").style.width = "150px";
        for(var el of document.getElementsByClassName("main")){
        el.style.marginLeft = "150px";
        }
        document.body.style.backgroundColor = "rgba(0,0,0,0)";
    }
    
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        for(var el of document.getElementsByClassName("main")){
        el.style.marginLeft = "0";
        }    document.body.style.backgroundColor = "black";
    }
    function setLoader(){
        if(loader){
            document.getElementsByClassName('loader')[0].style.display = 'block';
            loader = false;
        }
        else{
            document.getElementsByClassName('loader')[0].style.display = 'none';
            loader = true;
        }
        
    }
    </script>
    <nav>
        <div id="mySidenav" class="sidenav">
            <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
            <a href="#results">Prediction</a>
            <a href="#locations">Locations</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
          </div>
    </nav>
    <main>
        <div class = "main">
            <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776;</span>
            <h1>Snow Day Predictor</h1>
            <p>Select your location to continue</p>
            <input id = 'search' type="text">
            <button onclick ="self.getLocations(document.getElementById('search').value)">Search for this location</button>
            <p>Results</p>
            <ol id = "results">
                Click on a result below
            </ol>
            <div class="loader"></div>

            <h3>Load Data</h3>
            <button onclick='self.getSnowPrediction()'>Load snow day prediction</button>
        </div>
        <div class = "main" style="background-color: rgb(109, 0, 182);">
            <h1>Location Status</h1>
            <div id="locations">
                <p>No locations saved. Please choose a location above</p>
            </div>
            <button onclick='self.clear()'>Clear all locations</button>
        </div>
        <div class="main" style="background-color: rgb(71, 104, 255);">
            <h1>Predicted Snowfall</h1>
            <div id="snowfall">
                Select a location to continue <i class="far fa-snowflake"></i>
            </div>
        </div>
        <div class="main" id = "about" style="background-color: black">
            <h1>About</h1>
            <p>This project was made to predict the chance of a school closure aka snow day</p>
            <p>It is not infallible and should not be used in the place of an official announcment</p>
        </div>
        <div class="main" id = "contact">
            <h1>Contact</h1>
            <p>Contact at snowdaypredictor@gmail.com</p>
        </div>
    </main>


    <style>
html {
  scroll-behavior: smooth;
}
body {
    font-family: Arial, Helvetica, sans-serif;
    background-color:rgb(0,0,0);
    transition: background-color .5s;
    color: white;
}
span{
    color: white;
}  
.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #111;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}
  
.sidenav a {
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 20px;
    color: #818181;
    display: block;
    transition: 0.3s;
}
  
.sidenav a:hover {
    color: #f1f1f1;
}
  
.sidenav .closebtn {
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 10px;
}

button{
    background: none;
    margin:5px;
    border-radius: 5px;
    border: 2px solid white;
    color: white;
    padding: 5px;
}
input{
    border-radius: 5px;
    border: 2px solid black;
    outline: none;
    padding:2px;
}
.main {
    transition: margin-left .5s;
    padding: 16px;
    background-color: rgb(42, 42, 134);
    border-radius: 5px;
    margin-bottom: 10px;
}
.main li{
    margin-top: 30px;
    list-style: none;
}.main a{
    text-decoration: none;
    color: white;
    padding: 5px;
    border: 2px solid white;
    border-radius: 5px;
}
.loader {
    display: none;
    margin-left: 40px;
    border: 5px solid #f3f3f3;
    border-radius: 50%;
    border-top: 5px solid #3498db;
    width: 30px;
    height: 30px;
    -webkit-animation: spin 2s linear infinite; /* Safari */
    animation: spin 2s linear infinite;
}
@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
@media screen and (max-height: 450px) {
    .sidenav {padding-top: 15px;}
    .sidenav a {font-size: 18px;}
}
    </style>
""" 
    agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    async def reset(self):
        await self.js.recieve("Location Saved: click load snow day prediction", "results")
        await self.js.recieve("Location has been saved", 'locations')
        await self.js.recieve("Click load snow day prediction above", 'snowfall')
    def splitURL(self, response, string1, string2):
        split = response.split(string1)
        split.insert(1, string2)
        return "".join(split)

    async def getSnowAmount(self):
        r1 = urllib.request.Request(f"https://www.accuweather.com{open('locationKeys.txt', 'r').read()}", None, self.agent)
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
        r1 = urllib.request.Request(f"https://www.accuweather.com{open('locationKeys.txt', 'r').read()}", None, self.agent)
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
        agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        r1 = urllib.request.Request(f"https://www.accuweather.com/en/search-locations?query={search.replace(' ', '+')}", None, headers=agent)
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