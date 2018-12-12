# 1. merging dict
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {**x, **y}
print("1. Merged: %s" %z)

# 2. How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 7, 'aa': 13}
XS = sorted(xs.items(), key=lambda x: x[1])
print("2.1 Sorted (ascending values): %s" %XS)
import operator
XS = sorted(xs.items(), key=operator.itemgetter(0))
print("2.2 Sorted (ascending keys): %s" %XS)

# 3. Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
print("3. Different ways to test multiple flags at once in Python:")
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')
# These only test for truthiness:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')

    