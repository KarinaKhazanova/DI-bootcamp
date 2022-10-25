// Retrieve the form and console.log it.

const rform = document.getElementsByTagName('form');
console.log (rform[0])


// Retrieve the inputs by their id and console.log them.

console.log (rform[0].fname)
console.log (rform[0].lname)
console.log (rform[0].submit)


// Retrieve the inputs by their name attribute and console.log them.

console.log (rform[0].elements['fname'])
console.log (rform[0].elements['lname'])

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

form.addEvenrListener("submit",form1);
function form1(event){
    event.preventDefault();
    let name = form.fname.value;
    console.log(name);
    let name2 = form.lname.value;
    console.log(name2);
    if(name.trim().length > 0 && name2.trim().lenght > 0){
        const ul=document.querySelector("ul");
        let li=document.createElement("li");
        li.textContent=name;
        ul.appendChild(li);

        let li2 = document.createElement("li");
        li2.textContent = name2;
        ul.appendChild(li2)
    }
}