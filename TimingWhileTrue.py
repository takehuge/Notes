import dis

def while_one():
    while 1:
        pass

def while_true():
    while True:
        pass

if __name__ == "__main__":
    print("while_one\n")
    dis.dis(while_one)
    
    print("while_true\n")
    dis.dis(while_true)

# Timing part
import timeit

def while_one_tim():
    i = 0
    while 1:
        i += 1
        if i == 10000000:
            break

def while_true_tim():
    i = 0
    while True:
        i += 1
        if i == 10000000:
            break

if __name__ == "__main__":
    w1 = timeit.timeit(while_one_tim, "from __main__ import while_one", number=3)
    wt = timeit.timeit(while_true_tim, "from __main__ import while_true", number=3)
    print("while one: %s\nwhile_true: %s" % (w1, wt))

