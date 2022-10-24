let allBooks = [{
    title: "Harry Potter",
    author: "JK Rolling",
    image: "https://images.app.goo.gl/ixdbgY9RGEkgRXyP6",
    alreadyRead: true
},
{
    title: "Lord of the rings",
    author: "JRR Tolkien",
    image: "https://images.app.goo.gl/TukXiZGf3nvMmvzC7",
    alreadyRead: true
}]

const div = document.querySelector("div.listBooks")

let table = document.createElement("table")
div.appendChild(table)
let tbody = document.createElement("tbody")
let thead = document.createElement("thead")
let theadRow = document.createElement('tr')
const names = ['title', "author", "image"]
names.forEach(function (name) {
    let th = document.createElement('th')
    th.textContent = name
    theadRow.appendChild(th)
})
thead.appendChild(theadRow)
table.appendChild(thead)
table.appendChild(tbody)


allBooks.forEach(function (book) {
    let bookRow = document.createElement("tr")

    let titleCol = document.createElement("td")
    titleCol.textContent = book.title
    bookRow.appendChild(titleCol)

    let authorCol = document.createElement("td")
    authorCol.textContent = book.author
    bookRow.appendChild(authorCol)

    let imgCol = document.createElement("td")
    let img = document.createElement('img')
    img.src = book.image
    img.width = 100
    imgCol.appendChild(img)
    bookRow.appendChild(imgCol)

    if (book.alreadyRead) {
        bookRow.style.backgroundColor = "red"
    }

    tbody.appendChild(bookRow)

})