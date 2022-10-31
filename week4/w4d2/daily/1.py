number = int(input("Number: "))
length = int(input("Length: "))

result = []
total = 0
for _ in range(length):
    total += number
    result.append(total)

print(result)
