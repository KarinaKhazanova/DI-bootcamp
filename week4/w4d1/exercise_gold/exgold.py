print("hello world\n"*4, "I love python\n"*4)


month = int(input("Please enter number of the month: "))
if month >= 3 and month <=5:
    print("It is spring")
elif month >=6 and month <=8:
    print("It is summer")
elif month >=9 and month <=11:
    print("It is fall")
elif month <=2 or month == 12:
    print("It is winter")