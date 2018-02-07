import math

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

Survey()

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

SurveyCalibration()

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

survey()












