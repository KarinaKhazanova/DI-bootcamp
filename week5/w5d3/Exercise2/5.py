import datetime
def january():
    print(f'The 1st of January is in {datetime.datetime(2023, 1, 1)-datetime.datetime.today().replace(microsecond=0)}')

january()