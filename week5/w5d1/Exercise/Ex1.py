from functools import reduce

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Jerry', 3)
cat2 = Cat('Tom', 2)
cat3 = Cat('Batya', 5)


cats = [cat1, cat3,cat2]

# I
def oldest_cat_func(list_of_cats):
    oldest_cat = cats[0]

    for cat in list_of_cats:
        if oldest_cat.age < cat.age:
            oldest_cat=cat

    print(oldest_cat.name)


# II
oldest_cat_func = lambda cat1, cat2: cat1 if cat1.age > cat2.age else cat2
oldest_cat = reduce(oldest_cat_func, cats)

print(oldest_cat.name)