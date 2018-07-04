import json
import io
import struct

# Assembling data
x = [1, 2, 3, 4, 5, 6, 7, 8]
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
with open('data.txt', 'w') as txtfile:
    json.dump(data, txtfile) # dumps the dictionary as string format into memory

with open('data.txt') as txtfile:
    txt_loaded = json.load(txtfile)

print(txt_loaded['a list'][6])
print('David:',txt_loaded['David'])
print(txt_loaded)

# Write JSON=============================================================================
# -*- coding: utf-8 -*-

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(str_)

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

# print(data == data_loaded)
print(data_loaded['a list'][2])

# Write Binary file============================================================
with open('data.bin', 'wb') as binfile:
    # Convert dict to string first using ascii encoding
    datad = bytes(json.dumps(data), 'ascii')
    binfile.write(datad)
print("Content: " + " ".join(map(bin, datad)))

# Manipulating data type=======================================================
# dict to binary: (in string representation)
datastring = json.dumps(data)
databinary = ' '.join(format(ord(letter), 'b') for letter in datastring) #still a string displaying binary form
print('data in binary: ', databinary)
# binary to dict: (in string representation)
jsn = ''.join(chr(int(x, 2)) for x in databinary.split())
jsn = json.loads(jsn)  # <class 'dict'>
print('put back as dict: ', jsn)

# int to bytes:
x = 35
xbyte = x.to_bytes((x.bit_length() + 7) // 8, 'big') # byte length, byte order
print("binary for {} is: ".format(x, 'I'), ' '.join(map(bin, xbyte)))
y = x
ybyte = struct.pack(">I", y)
print("binary for %d is: " %(y), ' '.join(map(bin, ybyte)))
# byte to int:
bait = str(b'\x00\x10')
print(bait, " is: ", int.from_bytes(b'\x00\x10', 'big'))

