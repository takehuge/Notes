#DECORATOR & WRAPPER
import time
from functools import wraps

# CLASS DECORATOR
class decorator_class(object):
    def __init__(self, added_methodology):
        self.added_methodology = added_methodology
    def __call__(self, *a, **b):
        print('Call Method executed THIS before {}'.format(self.added_methodology.__name__))
        return self.added_methodology(*a, **b)


#Wrapping function with NO arguments
def decorator_func(added_functionality):
    def wrapper_func():
        print('wrapper executed THIS before {}'.format(added_functionality.__name__))
        return added_functionality()
    return wrapper_func

@decorator_func
def showing():
    print('SHOW TIME is ON')

@decorator_class
def showinG():
    print('SHOWING TIME is ON')

print('\nFUNCTION DECORATOR:')
showing()  # Basically it's equivalent to: showing = decorator_func(showing) "being WRAPPED or DECORATED"
print('\nCLASS DECORATOR:')
showinG()

#Wrapping function with arguments
def decorator_func01(added_functionality):
    def wrapper_func(*a, **b):
        print('wrapper executed THIS before {}'.format(
            added_functionality.__name__))
        return added_functionality(*a, **b)
    return wrapper_func

@decorator_func01
def showing_info(name, age, year):
    print('{} is {} year-old human being on this earth in {}'.format(name, age, year))

print('\nPASSING ARGUMENTS into WRAPPERS:')
showing_info('John', 101, 2416)

#Above is equivalent to:
def showing_INFO(name, age, year):
    print('{} is {} year-old human being on this earth in {}'.format(name, age, year))

print('\nwhich is equivalent to "function in function":')
decorator_func01(showing_INFO)('John', 101, 2416) #Function in function!

#Add arguments into decorator:
def decorator(arg1, arg2):    
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("Congratulations.  You decorated a function that does something with %s and %s" %(arg1, arg2))
            function(*args, **kwargs)
        return wrapper
    return real_decorator

@decorator("Facts", "Stories")
def print_args(*args):
    for arg in args:
        print(arg)

print('\nAdd arguments to Decorator:')
print_args(1,2,3,4,5)

#Second argument in the form of list or dictionary
def timetest(input_func):
    def timed(*args, **kwargs):
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        ))
        return result
    return timed

@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print("inside foobar")
    print(args, kwargs)


print('\nArguments in the form of List & Dictionary:')
foobar(["hello, world"], foo=2, bar=5)

# Function Decorator with Arguments
def decorators(arg1, arg2):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print("Arguements passed to decorator %s and %s" % ('arg1', arg2))
            function(*args, **kwargs)
        return wrapper
    return inner_function

@decorators("arg1", "arg2")
def print_argss(*args):
    for arg in args:
        print(arg)

print('\nPreserve informations about the function being passed:')
print(print_argss(1, 2, 3))
# @wraps preserves information about the function which is being passed:
print(print_argss.__name__)
print(print_argss.__doc__)

# Useful Applications:
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print('display_info ran with arguments ({}, {})'.format(name, age))


print('\nMy LOGTIMER:')
display_info('Tom', 22)
#EQUIVALENTLY
# display_info = my_logger(my_timer(display_info))
# display_info('Adam', 35)

print('\nEND\n')



