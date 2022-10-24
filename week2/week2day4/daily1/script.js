const promptWords = prompt().split(", ")

const maxLength = promptWords.reduce(
    function (a, b) {
        return a.length > b.length ? a : b;
    }
).length;

const firstAndLast = "*".repeat((maxLength + 4))
console.log(firstAndLast)
promptWords.forEach(function (item) {
    let spacesL = maxLength - item.length
    let spaces = ""
    if (spacesL > 0) spaces = " ".repeat(maxLength - item.length)
    console.log(`* ${item + spaces} *`)
})
console.log(firstAndLast)