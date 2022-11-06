class Farm:
    def __init__ (self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    

    def add_animal(self, name, amount):
        if name not in self.animals:
            self.animals[name] = amount
        else:
            self.animals[name] += amount


    def get_animal_types(self):
        type1 = []
        for animal in self.animals.keys():
            type1.append(animal)
        return type1


    def get_short_info(self):
       info = self.get_animal_types()
       return f"Macdonalds farm has {info}"

    






macdonald = Farm("macdonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep", 2)
macdonald.add_animal("goat", 12)

print(macdonald.animals)

print(macdonald.get_animal_types())


print(macdonald.get_short_info())



