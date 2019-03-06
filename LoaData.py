import json, io, os, struct, ast

# Assembling data
x = [1, 2, 3, 4, 5, 6, 7, 8]
data = {'a list': [u'€', u'輝', 1, 42, 3.141, 1337, 1.2345678e-13, 'help', True], #u'€'
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42},
        'David': x}
a_dict = {'new_key': 'new_value'}
e_dict = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 
          'y': [0, 2, 3, 5, 8, 12, 10, 13, 15, 17.9, 21, 25, 35]}
f_dict = {'z': [1.2345678e37, -8.234567e-37, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13]*1000}

data.update(a_dict)
data.update(e_dict)

print('\nWe are now using data comprising of %s character(s):' %len(str(data)))
print(str(data))

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
    datastring = bytes(json.dumps(data), 'ascii')  #Convert dict to string based on ascii
    bin_file.write(datastring)
with open('data.bin') as bin_file:
    bin_loaded = json.load(bin_file) #bin_file seems to be modified after being loaded
with open('data.bin','rb') as bin_file: #use rb to read as binary
    bin_read = bin_file.read()

print('\njson load BIN:')
print('same format after reloading? ', data == bin_loaded)
print(bin_loaded['a list'][i])
print('data.bin: David:', bin_loaded['David'])
ans = bin_loaded['David'][0] + bin_loaded['David'][6]
print('1 + 7 = ', ans)

print('\nDirect READ: bin_read (half of it): ', bin_read[:round(len(bin_read)/2)])
print('-> turned out to be just a string array!')
print('Converted to list:', str(bin_read).split(','))
print('\ne.g. the first element:')
print(str(bin_read).split(',')[0], ' ...which is weird!!!')

# Use UTF-8 encoding to build a file for <data>
datas = str(data)
print("\nSerialized Data (Length: %s): %s" %(len(datas), datas))
with open('data.utf', 'wb') as utfile:
    utfile.write(datas.encode('utf-8'))

# Comparing FILESIZE of the same content using 3 different approaches:
print("\nComparing FILESIZE:")
print('data.star: ', os.path.getsize('data.star'), 'bytes (txt: no indent, no sort)')
print('data.json: ', os.path.getsize('data.json'), 'bytes (json style, indented, sorted)')
print('data.bin: ', os.path.getsize('data.bin'), 'bytes (identical to txt)')
print('(whose byte-length is %s)' %len(bin_read))
datautfsize = os.path.getsize('data.utf')
print('data.utf: ', datautfsize, 'bytes (utf-8 encoding)\n')

# Manipulating data representation=======================================================
# mapping binary content of previous "datastring":
print("String representation of the Binary-Data (s-length: %s):" %len(str(datastring)))
print(str(datastring))
bin_groups = " ".join(map(bin, datastring)) #convert bytes-array to spaced-binary-string
print("Bytes-array of Binary-Data (length: %s):\n%s" %(len(bin_groups.split(" ")), bin_groups))
# dict to binary: (in string representation)
datastring = json.dumps(data)
print("\njson-dumps Data-String:\n %s" %datastring)
databinary = ' '.join(format(ord(letter), 'b') for letter in datastring) #still a string displaying binary form
print('data in binary:\n', databinary)
# binary to dict: (in string representation)
jsn = ''.join(chr(int(x, 2)) for x in databinary.split(' '))
jsn = json.loads(jsn)  # <class 'dict'>
print('\nput back as dict: ', jsn)

# Truncating and Appending to File's content:
from os import SEEK_END
from random import random as rd
with open('data.star', 'rb+') as star:
    steps = 2
    file_position = star.seek(-steps, SEEK_END)
    print("\nWe are now at position %s after %s step(s) back-seeking in data.star" %(file_position, steps))
    star.truncate()
    star.write(bytes(', ', 'ascii'))
    star.write(bytes('{:.0f}'.format(rd()*100), 'ascii'))
    star.write(bytes(']}', 'ascii'))

# Inserting IEEE-754 data
with open('data.utf', 'rb+') as star:
    steps = 1
    file_position = star.seek(-steps, SEEK_END)
    print("\nWe are now at position %s after %s step(s) back-seeking in data.utf" %(file_position, steps))
    star.truncate()
    star.write(bytes(", 'z':", 'ascii'))
    D = f_dict['z'] # it's a list
    s = struct.pack('>' + 'd'*len(D), *D) # f:32bit, d:64bit each floating-number
    print("\nwriting %s bytes into data.utf" %len(s))
    star.write(b'\x05' + s + b'\x06')
    star.write(bytes("}", 'ascii'))

print('After inserted d-64-array, data.utf: ', os.path.getsize('data.utf'), 'bytes (utf-8 encoding)\n')
floatsize = os.path.getsize('data.utf') - datautfsize - len(", 'z':") - 2
print("Float size of data of length %s is thus %s" %(len(D), floatsize))

# *** Read-out the IEEE-754 data-array ***
datastring = ''
with open('data.utf','rb') as bin_file: #use rb to read as binary
    bin_file.seek(0)
    full_read = bin_file.read()
    float_start = full_read.find(b'\x05') #ENQ (Enquiry)
    float_end = full_read.find(b'\x06') #ACK (Acknowledge)
    print("\nDouble-check the byte-size again:")
    print("IEEE-data starts from location-%s" %float_start)
    print("and it ends at location-%s\n" %float_end)
    bin_file.seek(0)
    bin_read = bin_file.read(float_start)
    datastring += bin_read.decode('utf-8')
    bin_file.seek(float_start+1) #skip floating-marker-byte \x07 (start)
    z_read = bin_file.read(float_end-float_start-1)
    print("The length of the floating-points: %s" %((float_end-float_start-1)//8))
    unfloat = struct.unpack('>' + 'd'*((float_end-float_start-1)//8), z_read) #unpacking IEEE-754 encoded float-points
    datastring += str(list(unfloat))
    bin_file.seek(float_end+1) #skip floating-marker-byte \x08 (end)
    bin_read = bin_file.read()
    datastring += bin_read.decode('utf-8')
    # print("data-string:\n %s" %datastring)

# Reconstructing byte-data into dictionary
data_reconstructed = ast.literal_eval(datastring)
print('data.utf: David:', data_reconstructed['David'])
ans = data_reconstructed['David'][0] + data_reconstructed['David'][6]
print('1 + 7 = ', ans)
print('data.utf: a list:', data_reconstructed['a list'])
print('data.utf: z[:12]:', data_reconstructed['z'][:12])
print('data.utf: z[2]+z[-1]: %s' %(data_reconstructed['z'][2] + data_reconstructed['z'][-1]))
print('data.utf: x:', data_reconstructed['x'])
print('data.utf: y:', data_reconstructed['y'])

# including f_dict of floating-list as char-list
data.update(f_dict)
datas = str(data)
# print("\nSerialized Data (Length: %s): %s" %(len(datas), datas))
with open('data.utfc', 'wb') as utfile:
    utfile.write(datas.encode('utf-8'))
print('\nAfter inserting f_dict as char-list, data.utfc: ', os.path.getsize('data.utfc'), 'bytes (utf-8 encoding)')
print('whose size is way larger if we have huge list of numbers!\n')
