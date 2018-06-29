# Manage TXT using different approach

text = 'Sample text to save\nNew line!'

saveFile = open('exampleFile.txt','w')

saveFile.write(text)
saveFile.close()

# Appending Files

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()

# Load TXT using numpy==============================================================
import numpy as np #looks like this only works for numbers but not string!

a = np.loadtxt("grade.txt")
print(a)
print(a[2, 1])

# Load TXT using csv==============================================================
import csv

with open('example.bin.txt', 'r') as myfile:
    rows = csv.reader(myfile, delimiter='\t')
    data = [row for row in rows]
    data_dict = dict()
    for i in data:
        data_dict[i[0]]=i[1]
    print(data_dict)
print(data)
