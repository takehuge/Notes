# This is to illustrate the concept between identity vs equality
# Identical means the two var are stored at the same memory location in contrary to equal
# sometime the system will optimize by storing some var in the same location

print("\nThis is how system optimize var memory storage:")
print("\nExample #1:")  # length of the number factors in
print("2**8 is 2**8: ", 2 ** 8 is 2 ** 8)
print("2**9 is 2**9: ", 2 ** 9 is 2 ** 9)
print("BUT")
print("2**8 == 2**8: ", 2 ** 8 == 2 ** 8)
print("2**9 == 2**9: ", 2 ** 9 == 2 ** 9)
print("\nExample #2:")  # length of the string factors in as well
print("'X'*10 is 'X'*10: ", 'X' * 10 is 'X' * 10)
print("'X'*30 is 'X'*30: ", 'X' * 30 is 'X' * 30)
print("BUT")
print("'X'*10 == 'X'*10: ", 'X' * 10 == 'X' * 10)
print("'X'*30 == 'X'*30: ", 'X' * 30 == 'X' * 30)
print("\nExample #2:") 
print("'public'*3 is 'public'*3: ", 'public' * 3 is 'public' * 3)
print("'public'*5 is 'public'*5: ", 'public' * 5 is 'public' * 5)
print("BUT")
print("'public'*3 == 'public'*3: ", 'public' * 3 == 'public' * 3)
print("'public'*5 == 'public'*5: ", 'public' * 5 == 'public' * 5)

print("\nIt matters HOW we get our string:")
print("\nExample #1:")
a, b = 'pub', ''.join(['p', 'u', 'b'])
print("Compare a =", a, " with b =", b)
print("a == b: ", a == b)
print("BUT a is b: ", a is b)
print("The memory location of a: ", id(a))
print("The memory location of b: ", id(b))

inputname = "David"
print("\nAnd also the OBJECT TYPE we use:")
yourinput = input("Please input " + "\"" + inputname + "\" : ")
print("Your input: ", yourinput)
print("yourinput == \"" + inputname + "\": ", yourinput == inputname)
print("BUT\nyourinput is \"" + inputname + "\": ", yourinput is inputname)

# Use sys.intern to force them into the same memory location
print("\nHowever, if we force them into the same memory location:")
from sys import intern
a, b = yourinput, inputname
print("BEFORE sys.intern, [id(a), id(b)]: ", [id(a), id(b)])
a, b = intern(yourinput), intern(inputname)
print("AFTER sys.intern, a is b: ", a is b)
print("Because NOW, [id(a), id(b)]: ", [id(a), id(b)], "\n")
