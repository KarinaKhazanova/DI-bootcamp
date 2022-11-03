from random import *

def get_random_temp():
    x = randint(-10, 40)  
    return(x)

get_random_temp()


def main():
    value = get_random_temp()
    print(f"The temperature right now is {value} degrees Celsius")
    if value < 0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif value >0 and value < 16:
        print('Quite chilly! Don’t forget your coat')
    elif value >= 16 and value <= 23:
        print('Chilly! Take sweater')
    elif value >= 24 and value <= 32:
        print('Great weather')   
    elif value > 32 and value < 40:
        print('Too hot! Do not forget sunscreen') 

    
    
main()

