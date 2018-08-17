import termios
attr = termios.tcgetattr(1)
attr[3] = attr[3] | termios.ECHO
termios.tcsetattr(1, termios.TCSANOW, attr)
