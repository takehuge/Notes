import json as js

# ASCII 
print("\nASCII DECimal for space is", ord(" "))
print("ASCII CHARacter for 32 is:", chr(32))

# ASCII Table
asciitab = {}
for i in range(128):
    asciitab[chr(i)] = i
print("\nASCII DICTIONARY:")
print(asciitab)
print("\nASCII TABLE:")
print(js.dumps(asciitab, indent=0, ensure_ascii=True))

# while True:
#     charac = input("Enter a CHARACTER:")
#     print("The corresponding DECIMAL is", asciitab[charac])

# BINARY vs DECIMAL
x = 137
print("\nDecimal %s is %s in binary" % (x, format(x, 'b')))
x = 1010100101011
print("\nBinary %s is %s in decimal" % (x, int(str(x), 2)))
x = 'c2bf'
print("\nHEX %s is %s in decimal" % (x, int(x, 16)))
x = '\uc2bf'
print("HEX %s is %s in decimal" % (x, ord(x)))

# UTF TABLE
unicodetab = {}
for i in range(1023):
    unicodetab[chr(i)] = i
print("\nUNICODE TABLE:")
print(js.dumps(unicodetab, indent=0))

