const div = document.querySelector("div")
div.style.backgroundColor = "lightblue"
div.style.padding = "20px"

const list = document.querySelector("ul")
list.children[0].style.display = "none"
list.children[1].style = "border: 1px solid black;"

document.body.style.fontSize = "20px"

if (div.style.backgroundColor === "lightblue") {
    alert(`Hello ${list.children[0].textContent} and ${list.children[1].textContent}`)
}