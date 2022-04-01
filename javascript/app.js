// Script to change each page
const sections = document.querySelectorAll('.section');
const sectBtns = document.querySelectorAll('.controls');
const sectBtn = document.querySelectorAll('.control');
const allSections = document.querySelectorAll('.main-content');

// Sets active classes apon page and button, removes unneeded active class
function PageTransations() {
    // Button active
    for (let i = 0; i < sectBtn.length; i++){
        sectBtn[i].addEventListener('click', function(){
            let currentBtn = document.querySelectorAll('.active-btn');
            currentBtn[0].className = currentBtn[0].className.replace('active-btn', '');
            this.className += ' active-btn';
        })
    }
    // Section active
    for (let i = 0; i < sectBtn.length; i++){
        sectBtn[i].addEventListener('click', (e)=>{
            const id = e.target.dataset.id;
            if(id){
                // Hide other sections
                sections.forEach((section) =>{
                    section.classList.remove('active');
                })

                const element = document.getElementById(id);
                element.classList.add('active')
            }
            else {
                console.log("ID Not Found")
            }
        })
    }
}

PageTransations();