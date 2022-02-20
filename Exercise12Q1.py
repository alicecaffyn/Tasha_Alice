cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# Q: what is wrong with this?
# A: adds the characters as string items in the list, rather than 'Oke'

# append used for one cheese
cheese.append('Oke')
print(cheese)

# extend used for multiple items
cheese.extend(['Oke', 'Gouda'])
print(cheese)