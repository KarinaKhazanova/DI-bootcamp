toppings = []


while True:
    pizza = input("Write what topping you want, when done write quit: ")
    if pizza.lower() != "quit":
        print(f"we will add {pizza} to your pizza")
        toppings.append(pizza)
    else:
        total = 10+(2.5*len(toppings))
        print(f"Your toppings are {toppings} and your total is {total}")
        break










