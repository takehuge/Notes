# import matplotlib.pyplot as plt
import json
from nltk.data import retrieve

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
data['Honey'] = 7000

data = json.dumps(data)
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


