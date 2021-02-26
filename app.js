function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
    for(var el of document.getElementsByClassName("main")){
      el.style.marginLeft = "150px";
    }
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    for(var el of document.getElementsByClassName("main")){
      el.style.marginLeft = "0";
    }    document.body.style.backgroundColor = "white";
  }