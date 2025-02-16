# Examples on dict
# https://realpython.com/python-dicts/

pets = {'cats': 5, 'dogs': 2, 'rabbits': 8}
print(pets) # will print the directory
print(pets['cats']) # 5
print(pets['cats'] > pets['dogs']) # True
print('cats' in pets) # True
print('pandas' in pets) # False
('horses' not in pets) # True
# pets['horses'] # KeyError
print(len(pets)) 
print(pets.get('cats')) # get value - 5
print(pets.get('zebras')) # None
#pets.items() returns a list of key-value pairs in a dictionary

for pet, number in pets.items():
    print('I have', number, pet)

print(pets.keys()) # returns alist of keys
print(pets.values()) # returns a list of values

pets2 = {'mouses':8, 'dogs': 101}
print(pets2)
pets.update(pets2) # will merge it with pets, if keyword already exists, the value will be updated
print(pets)  

pets.pop('rabbits') # removes a key from a dictionary, if it is present, and returns its value
print(pets)

pets.clear() # will delete the directory
print(pets) # {}

# New features from Python 3.9:
pets = {'cats': 5, 'dogs': 101, 'rabbits': 8}
pets2 = {'turtles': 42}
print(pets | pets2)
pets |= pets2
print(pets)

