# Examples on sets
# https://realpython.com/python-sets/

x = {'foo', 'bar', 'baz'}
print(len(x)) # 3
print('bar' in x) # True
print('spam' in x) # False

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

print(x1.union(x2)) # or x1 | x2 - {'foo', 'qux', 'quux', 'baz', 'bar'}

print(x1.intersection(x2)) # or x1 & x2 - {'baz'}

print(x1.difference(x2)) # or x1 - x2 - {'foo', 'bar'}

print(x1.symmetric_difference(x2)) # or x1 ^ x2 - {'foo', 'qux', 'quux', 'bar'}

x3 = {'foo', 'bar'}
print(x3.issubset(x1)) # or x3 <= x1 - True
print(x3.issubset(x2)) # False
print(x3 < x1) # a proper subset

print(x1.issuperset(x2))
print(x1 > x2)

x.add('eggs') # or x |= 'eggs'
print(x)

x.update(['fries', 'ham', 'eggs'])
print(x)

# be careful with update - without [], it will split the strings into characters!
print(x1)
x1.update('drink')
print(x1)

x.remove('bar') # or x.discard()
print(x)

x.clear()
print(x)
