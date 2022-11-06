class Dog:

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")

    def __str__(self):
        return f"{self.name}, {self.height}"
        
davids_dog = Dog('Rex', 50)

print(davids_dog)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog)
sarahs_dog.bark()
sarahs_dog.jump()

bigger_dog = sarahs_dog.name if sarahs_dog.height > davids_dog.height else davids_dog.name

print(bigger_dog)

