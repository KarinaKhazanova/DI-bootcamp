let colors = ["pink", "yellow", "purple", "red", "white"]

let suffixes = ["st", "nd", "rd", "th"]



for (var i = 0;1 < colors.length;i++){
    console.log(`My #${i+1} choice is ${colors[i]}`)
}

// bonus


for (var i = 0; i< colors.length; i++) {
    if(i < 3){
        console.log(`My ${i+1}${suffixes[i]} is ${colors[i]}`)
    }
    else {
        console.log(`My ${i+1}${suffixes[3]} is ${colors[i]}`)
    }
}