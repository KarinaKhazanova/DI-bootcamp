from codecs import charmap_build

mystring = input("Enter 10 character string please: ")

if len(mystring) < 10:
    print("string is not long enough")
elif len(mystring) > 10:
        print("string is too long")

print(mystring[0],mystring[9])

'''
another solution
print("firsr char:", mystring[0])
print("second char:", mystring[-1])
'''

for i in range (len(mystring)):
    print(mystring[:i+1])


''' another solution
for c in mystring:
temp_str +=
print(temp_str)'''

import random 
l = list(mystring)
random.shuffle(l)
result = ''.join(l)
print(result)


