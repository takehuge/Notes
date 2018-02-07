import json
import io

x = [1, 2, 3, 4, 5, 6, 7, 8]
# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€', True],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42},
        'David': x}

a_dict = {'new_key': 'new_value'}
data.update(a_dict)

# Use JSON to write txt file======================================================
# data = [1, 2, 3, 4, 5]
with open('no.txt', 'w') as txtfile:
    json.dump(data, txtfile)

with open('no.txt') as txtfile:
    txt_loaded = json.load(txtfile)

print(txt_loaded['a list'][6])
print('David:',txt_loaded['David'])
print(txt_loaded)

# JSON=============================================================================
# -*- coding: utf-8 -*-

# Make it work for Python 2+3 and with Unicode
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

# print(data == data_loaded)
print(data_loaded['a list'][2])

# Load TXT using numpy==============================================================
import numpy as np

a = np.loadtxt("grade.txt")
print(a)
print(a[2,1])

