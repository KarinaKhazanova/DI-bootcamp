import random 

def number():
     x = random.randint(1, 100)
     y = int(input('write a number between 1 and 100:'))

     if x == y:
         print('winner')
     else:
         print('not the same')
number()