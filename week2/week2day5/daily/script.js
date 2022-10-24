let numberBottles = Number(prompt("Number to begin counting down bottles"))

console.log(`${numberBottles} bottles of beer on the wall`)
console.log(`${numberBottles} bottles of beer`)
let sub = 1
numberBottles -= sub
for (numberBottles; numberBottles >= 0; numberBottles -= sub) {
    const itThem = sub === 1 ? "it" : "them"

    console.log(`Take ${sub} down, pass ${itThem} around`)
    if (numberBottles == 0) {
        console.log("0 bottle of beer on the wall")
        break
    }
    console.log(`${numberBottles} bottles of beer on the wall`)
    console.log(`${numberBottles} bottles of beer on the wall`)
    console.log(`${numberBottles} bottles of beer`)
    sub += 1
    if (sub > numberBottles) {
        sub = numberBottles
    }

}