const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
fruits.sort();

fruits.push ('Kiwi');

fruits.splice (0, 1);



console.log (fruits);

fruits.sort(function (a, b) {
    if (a > b) {
        return -1;
    }
    if (b > a) {
        return 1;
    }
    return 0;
});
console.log(fruits);