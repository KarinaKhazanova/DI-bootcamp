function playTheGame() {
    const start = confirm("Start the game?")
    if (!start) {
        alert("No problem, Goodbye")
        return
    }
    const number = Number(prompt("Enter a number between 0 and 10"))
    if (!number) {
        alert("Sorry Not a number, Goodbye")
        return
    }
    if (number < 0 || number > 10) {
        alert("Sorry it’s not a good number, Goodbye")
        return
    }
    const computerNumber = getRandomInt(0, 10)
    console.log(computerNumber)
    compareNumbers(number, computerNumber)

}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
}

function compareNumbers(userNumber, computerNumber) {
    for (let index = 0; index < 3; index++) {
        if (userNumber === computerNumber) {
            alert("WINNER")
            return
        }
        if (userNumber > computerNumber)
            alert("Your number is bigger then the computer’s, guess again")
        if (userNumber < computerNumber)
            alert("Your number is smaller then the computer’s, guess again")
        userNumber = Number(prompt("Type new number"))
    }
    alert("Out of chances")
    return
}