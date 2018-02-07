import random
import sys
import os

print('11 // 2 = ', 11//2)
print('17 % 3 =', 17%3)

quote = "\"Always remember you are unique\""

multi_line_quote = '''\njust
like everyone else
period'''

print("%s %s %s" %('I like the quote', quote, multi_line_quote))
print('\n' * 3)
print("I don't like ", end="") #no new line
print("newlines")

var1 = "Hello"
var2 = "world"
print(var1, var2, '\n')

grocery_list = ['apple', 'banana', 'papaya', 'watermelon']
todo_list = ['washing car', 'pick up kids', 'cooking nice meal']
event_list = grocery_list + todo_list
print('using plus sign:', event_list, '\n')
print('length: ', len(event_list))
event_list =[todo_list , grocery_list] #only take first list as global
print('\n', 'list within list: ', event_list)
print('\n', 'zoom in: ', event_list[1][2]) # zoom in
event_list[1] = event_list[1] + (['Working', 'Loving'])
print('\n', 'plus some items: ', event_list)
todo_list.insert(2, "Pickles")
print('\n', 'after update todo list, event: ', event_list)
grocery_list.insert(2, "Orange")
print('\n', 'after update grocery list, event: ', event_list)
event_list.append(['ball','shoes'])
print('\n', 'after append:', event_list)
event_list.extend(['bomb','rocket'])
print('\n', 'after extend: ', event_list)
todo_list.insert(1,"review article")
print('\n', 'checking todo list: ', todo_list)

x=2
y=3
z=x+y
x=100
print('\n', z) #proof that it only works on list