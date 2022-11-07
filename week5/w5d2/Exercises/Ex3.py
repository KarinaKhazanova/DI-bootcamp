import random

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f'{self.name} is barking')
    def run_speed(self):
        return f'{self.weight/self.age*10} is the speed of the dog'
    def fight(self, other_dog):
        running_speed = self.run_speed()
        if running_speed * self.weight > other_dog.running_speed() * other_dog.weight:
            return f'{self.name} is the winner'
        else:
            return f'{other_dog.name} is the winner'
class PetDog(Dog):
    def __init__(self,name,age,weight):
        super().__init__(name, age, weight)
        self.trained = False
    def train(self):
        self.trained = True
        self.bark ()
    def play(self):
        print(f'{self.name} all play together')
    def do_a_trick(self):
        if self.trained == True:
            x = random.randint(0,3)
            if x == 0:
                print(f'{self.name} does a barrel roll')
            elif x == 1:
                print(f'{self.name} stands on his back legs')
            elif x == 2:
                print(f'{self.name} shakes your hand')
            elif x == 3:
                print(f'{self.name} plays dead')
dog1 = PetDog('dog1', 1, 11)
dog2 = PetDog('dog2', 2, 22)
dog3 = PetDog('dog3', 3, 33)
dog1.train()
dog1.do_a_trick()