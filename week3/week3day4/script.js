const painting_size = 20*20;
const choice_size = 3*7;

let chosenColor = null;

const paintingSheet = document.querySelector(".painting_sheet");
const paintingColors = document.querySelector(".painting_colors");

for (let i = painting_size; i > 0; i--) {
    const paintingCell = document.createElement("div")
    paintingCell.className = "painting_cell"
    paintingCell.onclick = function () {
        paintingCell.style.backgroundColor = chosenColor
    }
    paintingSheet.appendChild(paintingCell)
}


function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

for (let i = choice_size; i > 0; i--) {
    const colorCell = document.createElement("button")
    colorCell.className = "painting_color"
    const color = getRandomColor()
    colorCell.style.backgroundColor = color

    colorCell.onclick = function () {
        chosenColor = colorCell.style.backgroundColor
    }


    paintingColors.appendChild(colorCell)
}

const clearButton = document.getElementById('clear')
clearButton.onclick = function () {
    paintingField.querySelectorAll(".painting_cell").forEach(function (cell) {
        cell.style.backgroundColor = "transparent"
    })
}




