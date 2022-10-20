const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let society = ""
const sortedNames = names.sort()

for (const name of sortedNames) {
    society =society + name[0]
}

console.log(society)