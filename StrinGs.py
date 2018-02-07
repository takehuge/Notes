#%%
import re

name = 'Einstein %s %d' % ('is', 100)
name0 = 'There are %(str1)s %(num)d people inside' % {
    'str1': 'almost', 'num': 1000}
i = 0
while i < len(name):
    print('Character %d is:' % i, name[i])
    i += 1
n = 1
for i in name0:
    print('Letter number %d is:' % n, i)
    n += 1

name1 = 'Einstein is a great international citizen, standing tall as giant'
results = [m.start() for m in re.finditer('al', name1)]
print(results)

s = 'percentage'
print("{} {} {:.2f}".format('Population', s, 13.75))

x=8
print("{:.2f}".format(x))
print("%.2f" %x)

print('\033[31m' + 'some red text') # use + to concatenate texts
print('\033[36;45;1m' + "Interesting")
print('\033[37m')  # and reset to default color

from colorama import init, Fore, Back, Style
init(autoreset=True) # more efficient this way
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
# Available formatting:
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

# import sys
from termcolor import colored
print(colored('Hello, World!', 'green', 'on_red'))
text = colored('Hello, World!', 'red', attrs=['bold'])
print(text)

from termcolor import cprint
cprint('Hello, World!', 'green', 'on_red')

if input('Clear Screen (y/any)?')=='y':
    # Clear Screen
    from time import sleep
    for i in range(100):
        # print('\033[2J') #alternative
        # print(chr(27) + "[2J")
        print('\x1b[2J\x1b[H') # works with colorama
        # print('\x1bc') # hexadecimal for ESC
        # print("\033c") # octal number for ESC in ASCII
        print(100-i)
        sleep(0.5)  # Time in seconds.

