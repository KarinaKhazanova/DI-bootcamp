// //Part I

// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.

const btn = document.getElementById("clear");
btn.addEventListener("click", start);

function start(){
    console.log("starting");
    setTimeout(helloWorld, 2000);
}

function helloWorld(){
    alert("Hello World")
}


// Part II

// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
setTimeout(addPara, 2000)
function addPara(){
const div =document.getElementById("container")
const addPara = document.createElement("p")
addPara.innerHTML = "Hello world";
div.appendChild(addPara)
}




// Part III

// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.



function addPara(){
    const div =document.getElementById("container")
    const addPara = document.createElement("p")
    addPara.innerHTML = "Hello world";
    div.appendChild(addPara)
    }
id = setInterval(addPara2, 2000)
let counter = 5;
function addPara2(){
    
    console.log("I work");
    if (counter > 0 ){
        const div =document.getElementById("container")
        const addPara = document.createElement("p")
        addPara.innerHTML = "Hello world";
        div.appendChild(addPara)
        counter--
    } else{
    clearInterval(id)
    }
    console.log(counter);
}


btn.addEventListener("click", clearInterval(id));

