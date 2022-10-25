// Using a DOM property, retrieve the h1 and console.log it.

const h1new = document.getElementsByTagName('h1')
console.log(h1new)

//Using DOM methods, remove the last paragraph in the <article> tag.
const art = document.querySelector("article");
art.removeChild(art.lastElementChild);

//Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
const newH2 = document.querySelector("h2")

newH2.addEventListener("click", changeToRed)
console.log(newH2)

function changeToRed(){
    newH2.style.background = "red";
}



//Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

const newH3 = document.querySelector("h3")
newH3.addEventListener("click", hide)

function hide(){
    newH3.style.display = "none";
}
//Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

const button1 = document.querySelector("button")
button1.addEventListener("click", bold)

function bold() {
    const allP=document.querySelectorAll("p")
    for (let i=0; i<allP.length; i++){
        allP[i].style.fontWeight="bold"
    }
}



//BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

//BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)