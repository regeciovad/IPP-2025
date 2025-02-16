# Examples on tuples
# https://realpython.com/python-lists-tuples/

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0]) # 'foo'
print(t[-1]) # 'corge'
#t[1] = 'hello' # TypeError: 'tuple' object does not support item assignment

for element in t:
    print(element)
