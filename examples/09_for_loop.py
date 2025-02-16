# for statements
# https://docs.python.org/3.8/tutorial/controlflow.html#for-statements

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for i in range(5):
    print(i) # will print 0 - 4

for i in range(5, 10):
    print(i) #5, 6, 7, 8, 9

for i in range(0, 10, 3):
    print(i) #0, 3, 6, 9


# this will not affect the for-loop
# because i will be overwritten with the next
# index in the range
for i in range(10):
    print(i)
    i = 5

a = [1, -2, 4, -3, -5, -44]
for x in a:
    if x < 0: a.remove(x)
print(a) # [1, 4, -5] some elements were skipped

a = [1, -2, 4, -3, -5, -44]
for x in a[:]: # create a local copy
    if x < 0: a.remove(x)
print(a) # [1, 4]
