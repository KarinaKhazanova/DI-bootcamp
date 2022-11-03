'''2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).'''

brand = {
    'name': 'Zara', 
    'creation_date': 1975, 
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000, 
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green'],
}}

'''3. Change the number of stores to 2.'''

brand['number_stores'] = 2
print(brand)


''' 4. Print a sentence that explains who Zaras clients are.'''

print(','.join(brand['type_of_clothes']))

'''5. Add a key called country_creation with a value of Spain.'''

brand['country_creation'] = 'Spain'
print(brand)

'''6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.'''

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
else:
    pass
print(brand)

'''7. Delete the information about the date of creation.'''

brand.pop('creation_date')
print(brand)

'''8. Print the last international competitor.'''

print (brand['international_competitors'][-1])



'''9. Print the major clothes colors in the US.''' 

print (brand['major_color']['US'])

'''10. Print the amount of key value pairs (ie. length of the dictionary).'''

len(brand)

print("Length: ", len(brand))

'''11. Print the keys of the dictionary.'''
for keys, value in brand.items():
   print(keys)



'''12. Create another dictionary called more_on_zara with the following details:'''

brand2 = {
    'creation_date': 1975, 
    'number_stores': 10000,
}

'''13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand. '''

brand.update(brand2)
print(brand)

