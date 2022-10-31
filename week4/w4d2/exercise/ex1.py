my_fav_numbers = {3, 5, 7, 9}

my_list = [4, 6]

my_fav_numbers.update(my_list)


print(my_fav_numbers)

my_fav_numbers.remove(9)

print(my_fav_numbers)

friend_fav_numbers = {2, 5, 6, 8}


our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("Union", our_fav_numbers)