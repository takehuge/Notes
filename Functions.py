def example():
    print('Basic Function')
    z = 3 + 9
    print(z)

# example()

def simple_addition(num1, num2):
    ans = num1 + num2
    print('num1 is',num1, 'num2 is', num2)
    print('The addition of them give:', ans)

# simple_addition(3,2)
# simple_addition(num2=4, num1=8) #variable can pick their own seat if declared explicitly in Python

# default

def simple(num1, num2=5):
    print(num1, num2)

# simple(2)

def basic_window(width, height, font='TNR',
                 bgc='w', scrollbar=True):
    """
    To illustrate Simple Window function
    """ #docstring
    print(width, height, font, bgc)

# basic_window(500, 350, 'a', 'b')
# basic_window(1000, 500, bgc='y')
# print(basic_window.__doc__)

# global vs local varibles
a = 10
x = 6
def example01():
    z = 5
    print(z)
    # print('local x can only be printed, i.e. non-operational:',x)
    global x
    x+=2
    print('global x is:',x)

# example01()

y = 9
def example02():
    globy = a
    print(globy)
    globy += 5
    print(globy)

    return globy

# z = example02()
# print(z)
# a+=12
# print(a)



