''' An integer is a number without a decimal point. A float is a floating-point number, which means it is a number that has a decimal place.'''


'''numpy.arange()'''

list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

num = 1.5
num_list = [num]
for i in range (7): 
    num += 0.5 
    num_list.append(num)
print(num_list)