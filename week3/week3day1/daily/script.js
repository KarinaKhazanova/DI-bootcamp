let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptun"]

function getRandomColor() {

    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
const listPlanets = document.querySelector('.listPlanets')
planets.forEach(function (planet) {
    const div = document.createElement("div")
    div.classList.add("planet")
    div.style.backgroundColor = getRandomColor()
    listPlanets.appendChild(div)
})