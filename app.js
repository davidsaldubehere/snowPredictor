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