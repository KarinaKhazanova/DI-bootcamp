from datetime import *
def today():
    print(date.today())
    print(f'The next holiday are in {date(2022, 12, 28)-date.today()}')

today()