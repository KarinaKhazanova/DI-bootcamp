from random import *

def random(number):
    x = randint(1, 100)  
    print(x)


    if number < 1:
        print('the number is too small')
    elif number > 100:
        print('the number is too big')
    elif number ==x:
        print('success')


random(25)








