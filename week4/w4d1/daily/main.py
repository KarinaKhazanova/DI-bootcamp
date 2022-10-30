from codecs import charmap_build

mystring = input("Enter 10 character string please: ")

if len(mystring) < 10:
    print("string not long enough")
elif len(mystring) > 10:
        print("string too long")

print(mystring[0],mystring[9])


for i in range (len(mystring)):
    print(mystring[:i+1])


import random 
l = list(mystring)
random.shuffle(l)
result = ''.join(l)
print(result)


