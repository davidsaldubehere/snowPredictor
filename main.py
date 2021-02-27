from guy import Guy
import lxml.html
from lxml.cssselect import CSSSelector
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
class Simple(Guy):
    __doc__="""
    <script>
    var els = [];
    var glinks;
    function recieve(value, target){
        document.getElementById(target).innerHTML = value;
        return "worked";
    }
    function recieveSearch(values, links){
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
                console.log(glinks[a]);
            });
        }
    }
    function openNav() {
        document.getElementById("mySidenav").style.width = "150px";
        for(var el of document.getElementsByClassName("main")){
        el.style.marginLeft = "150px";
        }
        document.body.style.backgroundColor = "rgba(0,0,0,0.6)";
    }
    
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        for(var el of document.getElementsByClassName("main")){
        el.style.marginLeft = "0";
        }    document.body.style.backgroundColor = "white";
    }
    </script>
    <nav>
        <div id="mySidenav" class="sidenav">
            <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
            <a href="#snowfall">Snow Amount</a>
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
            <button onclick ="self.getLocations(document.getElementById('search').value)">Add Location</button>
            <p>Results from search</p>
            <ol id = "results">
                Click on a result below
            </ol>
        </div>
        <div class = "main" style="background-color: rgb(109, 0, 182);">
            <h1>Current Locations</h1>
            <div id="locations">
                No locations selected
            </div>
            <button>Clear all locations</button>
        </div>
        <div class="main" style="background-color: rgb(71, 104, 255);">
            <h1>Predicted Snowfall</h1>
            <div id="snowfall">
                Select a location to continue
            </div>
        </div>
        <div class="main" id = "about">
            <h1>About</h1>
            <p>This project is powered by AccuWeather</p>
        </div>
        <div class="main" id = "contact">
            <h1>Contact</h1>
            <p>Contact at snowdaypredictor@gmail.com</p>
        </div>
    </main>


    <style>
    body {
    font-family: Arial, Helvetica, sans-serif;
    transition: background-color .5s;
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
    background: rgba(255, 255, 255, 0.623);
    border-radius: 2px;
    border: 2px solid black;
}
input{
    border-radius: 2px;
    border: none;
    outline: none;
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
  
@media screen and (max-height: 450px) {
    .sidenav {padding-top: 15px;}
    .sidenav a {font-size: 18px;}
}
    </style>
"""

    async def printS(self, value):
        testFile = open("locationKeys.txt", "a")
        testFile.write("Testing")
        testFile.close()
        print(await self.js.recieve("PYTHON RECIEVED"))
        print(await self.js.recieve("Reading file " + open("locationKeys.txt", "r").read()))
    
    async def getLocations(self, search):
        agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
        r1 = urllib.request.Request(f"https://www.accuweather.com/en/search-locations?query={search}", None, headers=agent)
        await self.js.recieve("right before attempt", "locations")
        response = (urllib.request.urlopen(r1).read())
        await self.js.recieve("got response", "locations")
        doc = lxml.html.fromstring(response)
        selAnchor = CSSSelector('a')
        foundElements = selAnchor(doc)
        found = [e for e in foundElements if "three" in str(e.get("href"))]
        text = [e.text_content().replace("\t", "").replace("\n", "") for e in found]
        links = [e.get("href") for e in found]

        await self.js.recieve("first", "locations")
        await self.js.recieveSearch(text, links)
        await self.js.recieve("second", "locations")

if __name__ == "__main__":
    x=Simple()
    x.serve()