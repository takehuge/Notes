    # Clear Screen
    for i in range(100):
        # print('\033[2J') #alternative
        # print(chr(27) + "[2J")
        print('\x1b[2J\x1b[H') # works with colorama
        # print('\x1bc') # hexadecimal for ESC
        # print("\033c") # octal number for ESC in ASCII
        print(i)