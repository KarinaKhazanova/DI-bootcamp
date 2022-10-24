
const div = document.getElementById("container");
console.log(div)

const lists = document.querySelectorAll(".list")
console.log(lists)

const list1 = lists[0]
const list2 = lists[1]

list1.children[1].textContent = "Richard"
list1.classList.add("university", "attendance")
lists.forEach(function (list) {
    list.classList.add("student_list")
    list.children[0].textContent = "Karina"
})

const list2Arr = Array.from(list2.children)
list2Arr.forEach(function (item) { if (item.textContent === "Sarah") list2.removeChild(item) })