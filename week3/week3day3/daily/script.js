const inputText = document.getElementById("input_text")

inputText.onkeydown = function (element) {
    const regexLetters = /[a-zA-Z]/;
    if (!regexLetters.test(element.key)) {
        element.preventDefault()
    }
}