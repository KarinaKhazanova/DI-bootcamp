const div = document.getElementById("navBar")
div.setAttribute("id", "socialNetworkNavigation")

let li = document.createElement("li")
const textNode = document.createTextNode("Logout")
li.appendChild(textNode)
const ul = document.querySelector("ul")
ul.appendChild(li)

console.log(ul.firstElementChild.textContent)
console.log(ul.lastElementChild.textContent)