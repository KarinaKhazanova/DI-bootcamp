family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = int()

for name, age in family.items():
    if age < 3:
        total +=0
    elif age >= 3 and age < 12:
        total += 10
    elif age >= 12:
        total += 15
        

print(f"your total is {total}")
        