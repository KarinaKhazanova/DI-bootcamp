function isDivisible() {
    let sum = 0;
    for (let number = 0; number < 500; number++) {
        if (number % 23 != 0) continue
        console.log(number)
        sum += number
    }
    console.log("Sum: " + sum)
}

isDivisible()