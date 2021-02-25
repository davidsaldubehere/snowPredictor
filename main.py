from guy import Guy
from datetime import datetime
import requests
import lxml

class Simple(Guy):
    __doc__="""
    <h1>Just a simple input test</h1>
    <input id = "input" >Search for your location</input>
    <button onclick = 'self.getLocations(document.getElementById("input").value)'>Search</button>
    <p id = "locations"></p>
    <script>
    function send(){
        self.printS(document.getElementById('input').value)
    }
    function recieve(value, target){
        document.getElementById(target).innerHTML = value;
        return "worked";
    }
    </script>
    """

    async def printS(self, value):
        testFile = open("locationKeys.txt", "a")
        testFile.write("Testing")
        testFile.close()
        print(await self.js.recieve("PYTHON RECIEVED"))
        print(await self.js.recieve("Reading file " + open("locationKeys.txt", "r").read()))
    
    async def getLocations(self, search):
        agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        response = requests.get(f"https://www.accuweather.com/en/search-locations?query={search}", headers=agent).text


if __name__ == "__main__":
    x=Simple()
    x.serve(autoreload=True)