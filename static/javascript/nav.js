// Created to allow the navigation bar to hide itself
// from the user untill user scrolls up over hover over nav

let lastScrollTop = 0;
const navbar = document.getElementById("navbar");
const hamburgerIcon = document.getElementById("hamburger-icon");
const hamburgerContainer = document.getElementById("hamburger-container")

// Adaptive navbar
window.addEventListener("scroll", () => {
    let scrollTop = window.scrollY || document.documentElement.scrollTop;

    // Hides navbar + hamburger on scroll
    if (scrollTop > lastScrollTop){
        navbar.style.top="-3rem";
        hamburgerContainer.style.right="-7rem";
    // Brings navbar into view on scroll-up, hides hamburger
    } else {
        navbar.style.top="0";
        hamburgerContainer.style.right="-7rem";
    }
    lastScrollTop = scrollTop;
})

// Shows navbar on mouseover
navbar.addEventListener("mouseover", () => {
    if (navbar.style.top="-3rem") {
        navbar.style.top="0";
    }
})

// Mobile hamburger
// Shows hamburger on click of hamburger-icon
hamburgerIcon.addEventListener("click", () => {
    hamburgerContainer.style.right="0rem";
})