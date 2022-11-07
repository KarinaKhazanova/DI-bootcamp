class Dog():
     def __init__(self, name, age, weight):
         self.name = name
         self.age = age
         self.weight = weight
     def bark(self):
         return f'{self.name} is barking'
     def run_speed(self):
         return f'{self.weight/self.age*10} is the speed of the dog'
     def fight(self, other_dog):
         running_speed = self.run_speed()
         if running_speed * self.weight > other_dog.run_speed() * other_dog.weight:
             print(f'{self.name} is the winner')
         else:
             print(f'{other_dog.name} is the winner')
             dog1 = Dog('dog1', 1, 11)
 dog2 = Dog('dog2', 2, 22)
 dog3 = Dog('dog3', 3, 33)
 dog1.fight(dog2)
 dog2.fight(dog3)