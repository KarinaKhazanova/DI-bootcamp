from faker import Faker

faker = Faker()
users = []
dict = {}
def faker_add(amount):
     for i in range(amount):
         dict['name'] = faker.name()
         dict['address'] = faker.address()
         dict['language_code'] = faker.language_code()
         users.append(dict)
     print(users)
   
faker_add(5)