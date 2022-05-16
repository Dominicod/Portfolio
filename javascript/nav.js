// Created to allow the navigation bar to hide itself
// from the user untill user scrolls up over hover over nav

let lastScrollTop = 0;
const navbar = document.getElementById("navbar");
window.addEventListener("scroll", () => {
    let scrollTop = window.scrollY || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop){
        navbar.style.top="-3rem";
    } else {
        navbar.style.top="0";
    }
    lastScrollTop = scrollTop;
})

navbar.addEventListener("mouseover", () => {
    if (navbar.style.top="-3rem") {
        navbar.style.top="0";
    }
})