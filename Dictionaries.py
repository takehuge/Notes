import matplotlib.pyplot as plt

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

# plt.bar(range(len(H)), H.values(), align='center')
# plt.xticks(range(len(H)), H.keys())
# plt.show()

