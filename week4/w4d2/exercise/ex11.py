sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]


sandwich_orders.append("Pastrami sandwich")
sandwich_orders.append("Pastrami sandwich")

finished_sandwiches = []
print("deli has run out of pastrami")
index = 0
while index < len(sandwich_orders):
    sandwich = sandwich_orders[index]
    index += 1
    if sandwich.find("Pastrami") != -1:
        continue
    finished_sandwiches.append(sandwich)


for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")
