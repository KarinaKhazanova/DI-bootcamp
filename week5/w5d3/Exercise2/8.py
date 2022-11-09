from datetime import *
​
def how_old_are_you(age, planet = "Earth"):
    hours_second = 31557600
    orbital_period = {
        "Earth" : 1.0,
        "Mercury" :  0.2408467,
        "Venus" : 0.61519726,
        "Mars" : 1.8808158,
        "Jupiter" : 11.862615,
        "Saturn" : 29.447498,
        "Uranus" : 84.016846,
        "Neptune" : 164.79132
    }
    
    k = hours_second * orbital_period[planet]
    return age / k

list_planet = ["Earth", "Mercury", "Venus", "Mars","Jupiter","Saturn", "Uranus","Neptune"]

for i in list_planet:
    print(f'on planet{i} you will be {how_old_are_you(21)}')