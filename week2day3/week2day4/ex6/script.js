function hotelCost() {
    let nights = NaN
    const perNight = 140
    while (isNaN(nights) || nights == 0) {
        nights = Number(prompt("number of nights they would like to stay in the hotel"))
    }
    return perNight * nights
}

// console.log(hotelCost())
function planeRideCost() {
    const dests = {
        "London": 183,
        "Paris": 220,
        "others": 300
    }
    let dest = ""
    while (!isNaN(Number(dest))) {
        dest = prompt("Destination")
    }
    let result = dests[dest]
    if (isNaN(result)) result = dests["others"]
    return result
}

//console.log(planeRideCost())

function rentalCarCost() {
    let days = NaN
    const perDay = 40
    while (isNaN(days) || days == 0) {
        days = Number(prompt("Car rental days:"))
    }
    let sum = perDay * days
    let discount = 0
    if (days > 10) discount = sum * 5 / 100
    return sum - discount
}

function totalVacationCost() {
    const hotelC = hotelCost()
    const planeC = planeRideCost()
    const carC = rentalCarCost()
    console.log(`The car cost: $${carC}, the hotel cost: $${hotelC}, the plane tickets cost: $${planeC}.`)
    return hotelC + planeC + carC
}
console.log("Total cost is " + totalVacationCost())