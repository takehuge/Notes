# 1. merging dict
print("\n1. merging dict")
x = {'a':1, 'b':2}
y = {'c':3, 'd':4}
z = {**x, **y}
print("Merged: %s" %z)

# 2. How to sort a Python dict by value
print("\n2. How to sort a Python dict by value")
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 7, 'aa': 13}
XS = sorted(xs.items(), key=lambda x: x[1])
print("2.1 Sorted (ascending values): %s" %XS)
import operator
XS = sorted(xs.items(), key=operator.itemgetter(0))
print("2.2 Sorted (ascending keys): %s" %XS)

# 3. Different ways to test multiple flags at once in Python
print("\n3. Different ways to test multiple flags at once in Python:")
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')
# These only test for truthiness:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')

# 4. Using namedtuple is way shorter than defining a class manually:
print("\n4. Using namedtuple to quickly build a class")
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
print("my car's color: %s" %my_car.color)
print("my car's mileage: %s" %my_car.mileage)
# We get a nice string repr for free:
print("my_car:")
print(my_car)
# Like tuples, namedtuples are immutable:
try: my_car.color = 'blue'
except Exception as err: print("Error: %s" %err)

# 5. The get() method on dicts and its "default" argument
print("\n5. The get() method on dicts and its 'default' argument")
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert"}
def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")
print(greeting(382)) #"Hi Alice!"
print(greeting(333333)) # default: "Hi there!"

# 6. Why Python Is Great: Function argument unpacking
print("\n6. Why Python Is Great: Function argument unpacking:")
def myfunc(x, y, z):
    print(x, y, z)
tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}
print("unpacking tuple_vec:")
myfunc(*tuple_vec)
print("unpacking dict_vec:")
myfunc(**dict_vec)

