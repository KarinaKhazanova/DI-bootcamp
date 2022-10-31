word = input("Word: ")

result = word[0]
for symbol in word:
    if result[-1] == symbol:
        continue
    result += symbol

print(result)
