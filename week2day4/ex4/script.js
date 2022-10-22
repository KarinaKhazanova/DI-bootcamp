const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}

const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ["banana", "orange", "apple"]

function myBill() {
    bill = {}
    shoppingList.forEach(function (item) {
        if (stock[item] === 0) return
        if (!(item in bill)) bill[item] = 0
        bill[item] += prices[item]
        stock[item] -= 1
    })
    console.log(bill)
    console.log(stock)
}
myBill()