a_string = input("Write your favorite fruits separated by spaces: ")

separated_string =a_string.split(' ')
print(separated_string)

b_string = input("Write the name of any fruit: ")


if b_string in a_string:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")