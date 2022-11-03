users = ["Mickey","Minnie","Donald","Ariel","Pluto"]



'''


 print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}'''

d = {}

for i in users:
    d[i] = users.index(i)
print(d)



'''print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}'''

dict = {}
for i, value in enumerate(users):
  dict[i] = value
  
print(dict)

'''#3/ 

 print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}'''




idxs = list(range(len(users)))
d3 = sorted((value, index) for index, value in enumerate(users, idxs))


print(d3)