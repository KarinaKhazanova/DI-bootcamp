class Farm:
    def __init__ (self, farm_name):
        self.farm_name = farm_name
        self.animals = {}



    def add_animal(self, name, amount):
        if name not in self.animals:
            self.animals[name] = amount
        else:
            self.animals[name] += amount

macdonald = Farm("macdonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep", 2)
macdonald.add_animal("goat", 12)

print(macdonald.animals)