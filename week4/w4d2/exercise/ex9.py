total = 0

while True:
    string = int(input("How old is each member of the family?: "))
    if string == 0:
        print(total)
        break

    if string < 3:
        pass
    elif string >= 3 and string < 12:
        total += 10
        print(f"Your total is {total}")
    elif string >= 12:
        total += 15
        print(f"Your total is {total}")

names = ["John", "Jack", "Jane"]

for i in range(len(names)):
    age = int(input(f"Type age for {names[i]}: "))

    if 16 < age < 21:
        names.pop(i)

print(names)








