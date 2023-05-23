function darkMode() {
    document.querySelector("#darkMode_btn").style.display = 'none';
    document.querySelector("#lightMode_btn").style.display = 'block';
    document.querySelector('body').style.backgroundColor = 'black';
    document.querySelector('#heading_main').style.color = "white";
    document.querySelector('#nav').style.borderBottom = "2px solid white";
    var nav_btn = document.querySelectorAll('#nav_btn');
    nav_btn.forEach(function(nav_btn) {
    nav_btn.style.backgroundColor = "#929090";
    nav_btn.style.color = "white"});
    var main_btn = document.querySelectorAll('#main_btn');
    main_btn.forEach(function(main_btn) {
    main_btn.style.backgroundColor = "#929090";
    main_btn.style.color = "white"});
}

function lightMode() {
    document.querySelector("#darkMode_btn").style.display = 'block';
    document.querySelector("#lightMode_btn").style.display = 'none';
    document.querySelector('body').style.backgroundColor = 'white';
    document.querySelector('#heading_main').style.color = "black";
    document.querySelector('#nav').style.borderBottom = "2px solid black";
    var nav_btn = document.querySelectorAll('#nav_btn');
    nav_btn.forEach(function(nav_btn) {
    nav_btn.style.backgroundColor = "#e0dcdc";
    nav_btn.style.color = "black"});
    var main_btn = document.querySelectorAll('#main_btn');
    main_btn.forEach(function(main_btn) {
    main_btn.style.backgroundColor = "#e0dcdc";
    main_btn.style.color = "black"});
}