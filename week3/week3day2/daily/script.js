const button = getButton()
const shuffleButton = document.getElementById("shuffle")

button.addEventListener("click", handleClick)
shuffleButton.addEventListener ("click", shuffleStories)

function getFormValues() {
    const noun = document.getElementById("noun").value
    const adjective = document.getElementById("adjective").value
    const person = document.getElementById("person").value
    const verb = document.getElementById("verb").value
    const place = document.getElementById("place").value
    return { noun, adjective,person, verb}
}

functuin handleClick(e) {
    e.preventDefault()
    const {noun, adjective, person,verb, place} = getFormValues()
    if([noun,adjective,person,verb,place]).includes(""))return
    const story = writeStory()
    appendStoryToPage(story)
    )
}
])