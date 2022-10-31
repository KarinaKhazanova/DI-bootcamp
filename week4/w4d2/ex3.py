basket = ["Banana", "Apples", "Oranges", "Blueberries"]

del basket[0]
print(basket)

del basket[2]
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)

print(basket.count("Apples"))

basket.clear()
print(basket)