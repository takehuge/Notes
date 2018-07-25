import math, random, time, types
import numpy as np

condition = 1 
while condition < 10:
    print(condition)
    condition += 1

# while True: #infinite loop
#     print('doing stuff')

exampleList = [1,5,6,7,8,9,354,53,5]

for x in exampleList:
    print(x)  
    print('continue program') #indentation is important in python

print('out of for-loop')

for x in range(1,11):
	print(x)

# if statement
x = 5
y = 10
z = 22
a = 3

if y > 5:
    print('I got it right')

if z < y > x:
    print('nice work')

if a != z:
    print('not fair')

if z == x:
    print('twin brother')
else:
    print('not same!')

if x > y:
    print('x > y')
elif x < z:
    print('x < z')
elif 5 > 2:
    print('5 > 2')
else:
    print('error')

if 0:
    print('WTH')

#%% while try if
def Survey():
    
    print('1) Blue')
    print('2) Red')
    print('3) Yellow')

    while True:
        try:
            question = int(input('Out of these options\(1,2,3), which is your favourite?'))
            break
        except:
            print("That's not a valid option!")

    if question == 1:
        print('Nice!')
    elif question == 2:
        print('Cool')
    elif question == 3:
        print('Awesome!')
    else:
        print('That\'s not an option!')

# Survey()

#%% try break except (use dictionary)
def SurveyCalibration():

    def TwoPorts():
        print("let's have two ports")

    def Thru():
        print("please get through it!")

    options = {2: TwoPorts,
               1: Thru
              }
    while True:
        try:
            option_id = int(input('Which way? (1:Through, 2:Two-Ports)'))
            if option_id in (1, 2):
                break #escape from while loop
            else: print('Please select only the listed option!')
        except:
            print('Not a valid type!')

    return options[option_id]()

# SurveyCalibration()

#%% try raise except
def survey():
    print('1) Blue')
    print('2) Red')
    print('3) Yellow')

    ans = 0
    while not ans:
        try:
            ans = int(
                input('Out of these options\(1, 2, 3), which is your favourite?'))
            if ans not in (1, 2, 3):
                raise ValueError
        except ValueError as e:
            ans = 0
            print(e)

    if ans == 1:
        print('Nice!')
    elif ans == 2:
        print('Cool')
    elif ans == 3:
        print('Awesome!')
    return None

# survey()

datad = []
book = dict()
a, b = 0, 0 # Global value can't seem to pass into method's inside loop if undeclared explicitly
def gen():
    global a, b # comment this out if below (local var) is used instead
    # a, b = 0, 0
    for i in range(8):
        # book = dict() # append/insert/extend/: seem to make datad and book the same object, ergo need to be clear every round
        a += 1 #= random.uniform(-1, 1)
        b += 1 #= random.uniform(-1, 1)
        book['x'], book['y'] = a, b # w/o clearing every round, the book will duplicate itself (why?)
        # book = dict(x=a, y=b)
        print("before: datad: ", datad)
        datad[len(datad):] = [book]
        # datad.extend([book])
        # datad.insert(len(datad),book)
        # datad.append(book) #append/insert/extend/: need to have the dict clear every round
        # print("book: ", book)
        # print("datad[i]: ", datad[i])
        print("after: datad: ", datad)
    return i, datad
    
# gen()
ge = gen()
# print(gen())
print('datad:', datad)

#Local vs Global Variables
def f():
    global s # all s defined inside will be GLOBAL
    print(s)
    s = "That's clear." # This will be made global as well
    print(s)

s = "Python is great!"
f()
print(s)
s = "WHAT?!"
print(s)


def g():
    global a
    for i in range(5):
        # print(id(a))
        a += 2
        # print(id(a))
        print(i, a) # print is yield in display
        # yield / return as a conclusion of a method / function
        yield i, a # yield is print to value on the fly
        time.sleep(0.17)
    return i, a

a = 0 
print("\nRunning g():")
g()  # If yield preceding return, g() will be holding until being push
print("\nEven assigning value, it is still running:")
G = g() # comment yield out and this will be flowing
print("\n", type(G))
print("\nPushing value out using __next__():")
if type(G) == types.GeneratorType:
    print("\nGenerator is spitting one by one:")
    for i in range(5):
        print(G.__next__())
else: print("\nNo pushing-on-fly for RETURN, only spitting out TUPLE data")

print('\nUsing : as a copy to protect original var')
def func2(list):
    print(list)
    list += [47,11]
    print(list)

fib = [0, 1, 1, 2, 3, 5, 8]
print("Original fib:", fib)
func2(fib[:]) # using : to slice a copy
print("INTACT fib:", fib)
func2(fib)
print("MODIFIED fib:", fib)

print("\nAnother example:")
colours = ["red"]
for i in colours:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print("\nNo Slicing: ", colours)

colours = ["red"]
for i in colours[:]:
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print("\nINTACT: ", colours)

print("\nThis is to illustrate LOCAL precedes GLOBAL VAR:")
def fu():
    global s # This solves the problem
    print(s)
    s = "Me too." # +=, loop, assignment etc will change the var identity to LOCAL
    print(s)

s = "I hate spam." 
fu()
print(s)
    

