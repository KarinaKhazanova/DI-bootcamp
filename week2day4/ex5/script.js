function changeEnough(itemPrice, amountOfChange) {
    const quarters = amountOfChange[0] / 4
    const dimes = amountOfChange[1] / 10
    const nickels = amountOfChange[2] / 20
    const pennies = amountOfChange[3] / 100
    const sum = quarters + dimes + nickels + pennies
    return itemPrice < sum
}

console.log(changeEnough(14.11, [2, 100, 0, 0])) // returns false
console.log(changeEnough(0.75, [0, 0, 20, 5]))// returns true