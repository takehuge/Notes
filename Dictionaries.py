# import matplotlib.pyplot as plt
import json
from nltk.data import retrieve
from time import time, ctime
from os import SEEK_END

def Histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

name = 'Herr Albert Einstein is a Genius'
H = Histogram(name)
print(H)
print([x for x in H.keys()])
print([x for x in H.values()])

x_dict ={'a':1, 'b':2}
print('before update:', x_dict)
x_dict.update({'c':3})
print('after update:', x_dict)

# plt.bar(range(len(H)), H.values(), align='center')
# plt.xticks(range(len(H)), H.keys())
# plt.show()

data = dict()
data['David'] = 500000
data['Sam'] = 20000
data['Honey'] = '7000'
data = json.dumps(data) # convert it into a JSON string to be turned into binary later on
print("data after being json-dumped: %s" %data)

with open('data.star', 'wb') as file:
    file.write(bytes(data, 'utf8'))
file.close()
with open('data.star') as file:
    retrieve = file.read()
file.close()
print(retrieve)
d = {} # or dict()
for pair in retrieve.split(","):
    i = pair.split(":")
    d[i[0]] = i[1]

print(d)

# truncate the last letter from file
with open('data.star', 'rb+') as filehandle:
    filehandle.seek(-1, SEEK_END)
    filehandle.truncate()

adata = dict()
adata['Alien'] = 101
adata['Big'] = 3000
adata = json.dumps(adata)
adata = adata[1:-1]
# append to file
with open('data.star', 'ab+') as file:
    file.write(bytes(", ", 'ascii') + bytes(adata, 'ascii') + bytes("}", 'ascii'))

userlog = {
    'level_1a': 1,
    'level_1b': {
        'level_2a': 2,
        'level_2b': {
            'level_3a': 'genius',
            'IQ_level': {'David': 80000, 'Jane': 80, 'John': 137137 }
        }
    },
    'level_1c': {
        'level_2a': 2,
        'level_2b': {
            'level_3a': 'genius',
            'IQ_level': {'David': 80000, 'Jane': 80, 'John': 137137 }
        }
    }
}

for a, b in userlog.items():
    print('a: %s' %a)
    print('b: %s' %b)

# recursive method
def getpath(nested_dict, value, prepath=()):
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found the value!
            return path
        elif hasattr(v, 'items'): # see if v is a dick
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p # stop the recursive-loop if the value matched, else continue the for-loop

start = time()
print("Path: %s" %[x for x in getpath(userlog, 'genius')])
duration = time() - start
print("Recursive algo required %ss" %duration)


