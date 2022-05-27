// Creates fading in animations for portfolio page, using element
// and viewport positioning

window.addEventListener("scroll", appear);

function appear() {
    const appears = document.querySelectorAll(".appear");
    for (let i = 0; i < appears.length; i++) {
        let windowHeight = window.innerHeight;
        let elementTop = appears[i].getBoundingClientRect().top;
        const elementVisible = 150;

        if (elementTop < windowHeight - elementVisible) {
            appears[i].classList.add("inview");
        } else {
            appears[i].classList.remove("inview");
        }
    }
}

// Runs function at start of page load
appear()