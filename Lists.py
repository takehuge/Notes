import numpy as np
from Searching import locate

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print('my_list(1st method): ', my_list)
print('my_list(2nd method): ', *my_list)
print('my_list(3th method): ')
print(*my_list, sep=',')
print('my_list(4th method): ')
print(*my_list, sep='\n')
print('my_list(5th method): ')
print(','.join(map(str, my_list)))
print('my_list(6th method): ')
print('\n'.join(map(str, my_list)))
print('my_list(7th method): ')
print('\n=> '.join(['%.2f']*len(my_list)) % tuple(my_list))
print('my_list[0]:', my_list[0])
print('my_list[:-1]:', my_list[:-1])
print('my_list[0:8]:', my_list[0:8])
print('my_list[2:]:', my_list[2:])
print('my_list[:]:', my_list[:])
print('my_list[:6]:', my_list[:6])
print('my_list[2:-1:2]:', my_list[2:-1:2])
print('my_list[-1:2:-1]:', my_list[-1:2:-1])
print('my_list[8:1:-1]:', my_list[8:1:-1])
print('my_list[::-1]:', my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

# reverse the url
print(sample_url[::-1])

# Get the top level domain
print(sample_url[-4:])

#without http
print(sample_url[7:]);

#without both
print(sample_url[7:-4]);

# Appending
x = [3,4,5,6,8,1,6,88,2,4,9,6,0,4,5,6,7,8,5]
print("location of 5 in x: ", locate(5, x))
x.append(80)
print('x after appended by 80:', x)
print("Last x's element after appending:", x[len(x)-1])
x.insert(2,99)
print(x)
x.remove(x[1]) #or remove(4)
print(x)
print(x[5:9])
print(x[9:5:-1])
print("88 is of index", x.index(88), "in x") #return first index of value
print("6 is of index %s-th in x." % (x.count(6)))
x.sort()
print(x)
x.pop() #remove the last element
print("x had removed the last element:", x)

y = ['Janet', 'Jessy', 'Kelly', 'Alice', 'Joe', 'Bob']
y.sort(reverse=True) #sort alphabetically
print(y)

print('Multidimensional list')
x = [[5,6],[16,7],[8,2],[2.5,15]]
print(x[1])
print(x[1][0])
a = np.array(x) # convert list to numpy array
print('x[1][0] is', a[1,0])
y = [
    [[1,2],[3,4],[5,6]],
    [[7,8],[9,10],[11,12]],
    [[13,14],[15,16]],
    [17,18]
    ]
print(y)
print(y[2][1][1])

numseries = np.array(np.arange(1,100,2))
print(numseries)

#Transpose
print('original x:')
print([list(i) for i in x])
x_transposed = [list(i) for i in zip(*x)]
print('transposed x:\n', x_transposed)

# Tuples (Lists that is immutable)
tup0 = ()
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
tup5 = (50,)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56) # can be override
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100; # becoz it's immutable

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)
