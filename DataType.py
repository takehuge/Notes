import json as js
import struct

# ASCII 
print("\nASCII-order for <space> is", ord(" "))
print("ASCII CHARacter for 32 is:", chr(32))

# ASCII Table
asciitab = {}
for i in range(128):
    asciitab[chr(i)] = i
# print("\nASCII DICTIONARY:")
# print(asciitab)
# print("\nASCII TABLE:")
# print(js.dumps(asciitab, indent=0, ensure_ascii=True))

# UTF TABLE
unicodetab = {}
for i in range(1023):
    unicodetab[chr(i)] = i
# print("\nUNICODE TABLE:")
# print(js.dumps(unicodetab, indent=0))

# while True:
#     charac = input("Enter a CHARACTER:")
#     print("The corresponding DECIMAL is", asciitab[charac])

# DECIMAL convert to other base or encoding:
x = 105 #encoding position
print("\nDecimal %s is %s in decimal (base 10)" % (x, format(x, 'd')))
print("Decimal %s is %s in binary (base 2)" % (x, format(x, 'b'))) #conversion to bytes
print("Decimal %s is %s in binary (base 2)" % (x, bin(x)))
print("Decimal %s is %s in octet (base 8)" % (x, format(x, 'o')))
print("Decimal %s is %s in hex (base 16)" % (x, format(x, 'x')))
print("Decimal %s is %s in hex (base 16)" % (x, hex(x)))
print("Decimal %s is %s in HEX (base 16)" % (x, format(x, 'X')))
print("Decimal %s is %s in character (utf)" % (x, format(x, 'c')))
print("Decimal %s is %s in exponent (float)" % (x, format(x, '.3e')))
print("Decimal %s is %s in fixed-point (float)" % (x, format(x, '2.3f')))
print("Decimal %s is %s in fixed-point (float)" % (x, float(x)))
print("Decimal %s is %s in general (auto-float)" % (x, format(x, 'g')))

# Other bases changed back to decimal via 'int'
x = 1010100101011
y = int(str(x), 2)
print("\nBinary %s is %s in decimal" % (x, y))
print("which is %s back in binary" %[i for i in map(bin, [y])]) #used for iterable array cases
print("which is %s back in binary" %bin(y)) #used for non-iterables
x = 'c2bf'
y = int(x, 16)
print("\nHEX %s is %s in decimal" % (x, y))
print("which is %s back in hex" %hex(y))
print("which is %s back in hex" %[i for i in map(hex, [y])])
x = 0Xc2bf
y = str(x) #or int(x) directly
print("\nHEX %s is %s in decimal" % (hex(int(x)), y))
print("which is %s back in hex" %hex(int(y)))
print("which is %s back in hex" %[i for i in map(hex, [int(y)])])

#The ord() method returns an integer representing Unicode code point for the given Unicode character.
x = '\uc2bf' #unicode escape format
y = ord(x) #find the unicode-order first
print("\nUNICODE %s is Unicode-order of %s (decimal-format)" % (x.encode('unicode_escape'), y)) 
print("which can be converted back to UNICODE: %s" %chr(y)) 
x = '輝' #unicode escape format
y = ord(x) #find the unicode-order first
print("\nUNICODE %s is Unicode-order of %s (decimal-format)" % (x.encode('unicode_escape'), y)) 
print("which can be converted back to UNICODE: %s" %chr(y)) 
x = '中研院' #unicode escape format
y = [ord(x) for x in x] #find the unicode-order first
print("\nUNICODE %s is Unicode-order of %s (decimal-format)" % (x.encode('unicode_escape'), y)) 
print("which can be converted back to UNICODE: %s" %''.join([chr(y) for y in y])) 

# Direct number in different base and form
x = 0b101001000110
print("\nBinary 0b101001000110 is %s in decimal" %str(x))
x = 0X7fea1068c
print("\nHex 0X7fea1068c is %s in decimal" %str(x))
x = 2e-1
print("\nExp 2e-1 is %s in decimal" %str(x))

# int to bytes:
x = 35
xbyte = x.to_bytes((x.bit_length() + 7) // 8, 'big') # byte length, byte order
print("\nbinary for {} is: ".format(x), ' '.join(map(bin, xbyte)))
y = 35
ybyte = struct.pack(">I", y)
print("binary for %d is: " %(y), ' '.join(map(bin, ybyte)))
# byte to int:
bait = str(b'\x7f\x10')
print(bait, " is: ", int.from_bytes(b'\x7f\x10', 'big'))

# How information is encoded in bytes
s = '慧'
s = ord(s)
print("\nThe character %s has a bit-length of %s based on the order of %s" %(chr(s), s.bit_length(), s))
print("thus equivalently, the corresponding byte-length is %s byte(s)" %((s.bit_length() + 7) // 8))

s_encoded = chr(s).encode('unicode_escape') #conversion to bytes
print(type(s_encoded))
print("which can be encoded as %s in \\u for %s bytes" %(s_encoded, len(s_encoded)))
print("byte-array in binary: %s" %','.join(map(bin, s_encoded)))
print("another way, same meaning: %s\n" %bin(int.from_bytes(s_encoded, 'big')))

s_encoded = chr(s).encode('utf-8')
print("which can be encoded as %s in utf-8 for %s bytes" %(s_encoded, len(s_encoded)))
print("byte-array in binary: %s" %','.join(map(bin, s_encoded)))
print("another way, same meaning: %s\n" %bin(int.from_bytes(s_encoded, 'big')))

s_encoded = chr(s).encode('utf-16')
print("which can be encoded as %s in utf-16 for %s bytes" %(s_encoded, len(s_encoded)))
print("byte-array in binary: %s" %','.join(map(bin, s_encoded)))
print("another way, same meaning: %s\n" %bin(int.from_bytes(s_encoded, 'big')))

s_encoded = js.dumps(chr(s))
print("which can be encoded as %s in json.dumps for %s bytes" %(s_encoded, len(s_encoded)))

s_encoded = bytes(js.dumps(chr(s)), 'utf-8')
print("which can be encoded as %s in bytes(json.dumps) for %s bytes" %(s_encoded, len(s_encoded)))
print("byte-array in binary: %s" %','.join(map(bin, s_encoded)))
print("another way, same meaning: %s\n" %bin(int.from_bytes(s_encoded, 'big')))

# Encoding floating list:
D = [1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13, 1.234567e-13]
print("The length of D: %s" %len(str(D)))
s = struct.pack('f'*len(D), *D)
print(len(s))

from array import array as ar
float_array = ar('d', D)
print(len(float_array))
