let sentence = "The dinner is not that bad, I like it"
let wordNot = sentence.indexOf("not")
let wordBad = sentence.indexOf("bad")

console.log(wordNot);
console.log(wordBad);

if(wordBad > wordNot) {
    console.log(sentence.substring(0, wordNot) + " good " + sentence.substring(wordBad +3, sentence.length)); 
}


