class Zoo:
    def __init__(self, zoo_name):
        self.animals=[]
        self.zoo_name=zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            #self.animals = new_animal ('Dog')

            print(self.animals)

    def get_animals(self):
        print(self.animals)

    #def sell_animal(self, animal_sold):

    
    
ramat_gan_safari=Zoo('name')

ramat_gan_safari.add_animal("Dog")
ramat_gan_safari.get_animals("Lion")
ramat_gan_safari.get_animals()



Zoo.add_animal