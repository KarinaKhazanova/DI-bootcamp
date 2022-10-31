"""string = int(input("How old are you?: "))"""


import string



total = 0
while True:
    string = int(input("How old is each member of the family?: "))
    if string <3:
        pass
    elif string >=3 and string <12: 
        total +=10
        total +=15
        print(f"Your total is {total}")
    elif string>=12:
        total +=15
        print(f"Your total is {total}")








