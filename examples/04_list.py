# Eaxmples on lists
# https://realpython.com/python-lists-tuples/

a = ['foo', 'bar', 'baz', 'qux']
print(a)
print(a[0]) # 'foo'
print(a[-1]) # 'qux'
print(a[0:2]) # ['foo', 'bar']
print(len(a))
print('foo' in a) # True
print('spam' in a) # False

a[0] = 'spam'
print(a)

del a[3]
print(a)

#a += 42 # TypeError: 'int' object is not iterable
a += [42]
print(a)

#a += 'qux' # probably not what you want! This will add ['q', 'u', 'x']
a += ['qux']
print(a)

a.append('eggs') # add 1 element
print(a)

#a.append(['fries', 'ham']) # probably not what you want! Will create this: ['spam', ..., 'eggs', ['fries', 'ham']]
# for list, use extend:
a.extend(['fries', 'ham'])
print(a)

a.remove('ham')
print(a)
#a.remove('dog') # ValueError: list.remove(x): x not in list
