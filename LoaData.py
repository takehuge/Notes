import json, io, os, struct

# Assembling data
x = [1, 2, 3, 4, 5, 6, 7, 8]
data = {'a list': [1, 42, 3.141, 1337, 'help', u'€', True],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42},
        'David': x}
a_dict = {'new_key': 'new_value'}
e_dict = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
          'y': [0, 2, 3, 5, 8, 12, 10, 13, 15, 17.9, 21, 25, 35]}
data.update(a_dict)
data.update(e_dict)

i = 5 # index of dict of a list
# Use json to write txt file======================================================
with open('data.star', 'w') as txt_file:
    json.dump(data, txt_file) # dumps the dictionary as string format into memory
# Read txt file with json
with open('data.star') as txt_file:
    txt_loaded = json.load(txt_file)

print('\njson load TXT:')
print('same format after reloading? ', data == txt_loaded)
print(txt_loaded['a list'][i])
print('data.star: David:',txt_loaded['David'])
ans = txt_loaded['David'][0] + txt_loaded['David'][6]
print('1 + 7 = ', ans)

# Use json to Write JSON=============================================================================
with io.open('data.json', 'w', encoding='utf8') as json_file:
    json_string = json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
    json_file.write(json_string)
# Read JSON file with json
with open('data.json') as json_file:
    json_loaded = json.load(json_file)

print('\njson load proper-JSON:')
print('same format after reloading? ', data == json_loaded)
print(json_loaded['a list'][i])
print('data.json: David:', json_loaded['David'])
ans = json_loaded['David'][0] + json_loaded['David'][6]
print('1 + 7 = ', ans)

# Use wb to write json-style data============================================================
with open('data.bin', 'wb') as bin_file:
    datastring = bytes(json.dumps(data), 'utf8')  #ascii #Convert dict to string
    bin_file.write(datastring)
with open('data.bin') as bin_file:
    bin_loaded = json.load(bin_file) #bin_file seems to be modified after being loaded
with open('data.bin','r') as bin_file: #use rb to read as binary
    bin_read = bin_file.read()

print('\njson load BIN:')
print('same format after reloading? ', data == bin_loaded)
print(bin_loaded['a list'][i])
print('data.bin: David:', bin_loaded['David'])
ans = bin_loaded['David'][0] + bin_loaded['David'][6]
print('1 + 7 = ', ans)

print('\nDirect READ: bin_read (half of it): ', bin_read[:round(len(bin_read)/2)])
print('-> turned out to be just a string array!')
print('Converted to list:', bin_read.split(','))
print('\ne.g. the first element:')
print(bin_read.split(',')[0], ' ...which is weird!!!')

# Comparing FILESIZE of the same content using 3 different approaches:
print("\nComparing FILESIZE:")
print('data.star: ', os.path.getsize('data.star'), 'bytes (txt: no indent, no sort)')
print('data.json: ', os.path.getsize('data.json'), 'bytes (json style, indented, sorted)')
print('data.bin: ', os.path.getsize('data.bin'), 'bytes (identical to txt)\n')

# Manipulating data type=======================================================
# mapping binary content of previous "datastring":
print(datastring)
print("Binary Content of data:\n" + " ".join(map(bin, datastring)), '\n')
# dict to binary: (in string representation)
datastring = json.dumps(data)
databinary = ' '.join(format(ord(letter), 'b') for letter in datastring) #still a string displaying binary form
print('data in binary:\n', databinary)
# binary to dict: (in string representation)
jsn = ''.join(chr(int(x, 2)) for x in databinary.split())
jsn = json.loads(jsn)  # <class 'dict'>
print('\nput back as dict: ', jsn)

# int to bytes:
x = 35
xbyte = x.to_bytes((x.bit_length() + 7) // 8, 'big') # byte length, byte order
print("\nbinary for {} is: ".format(x), ' '.join(map(bin, xbyte)))
y = x
ybyte = struct.pack(">I", y)
print("binary for %d is: " %(y), ' '.join(map(bin, ybyte)))
# byte to int:
bait = str(b'\x00\x10')
print(bait, " is: ", int.from_bytes(b'\x00\x10', 'big'))
print('\n')

