from datetime import *
def bd (bd='26.04.01 17:56:55'):
     bd_obj = datetime.strptime(bd, '%d.%m.%y %H:%M:%S')
     today = datetime.now()
     print(f'You lived: {today - bd_obj}')
bd()
