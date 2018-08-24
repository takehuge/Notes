import ctypes
import numpy as np

a = "hello world"
print("\na equals hello world")
print("id(a):", id(a))
print("id(\"hello world\"):", id("hello world"))
print("Now get b to refer a")
b = ctypes.cast(id(a), ctypes.py_object).value
print("b equals",b)
print("id(b):", id(b))

a = 137
print("\na equals 137")
print("id(a):", id(a))
print("id(137):", id(137))
print("Now get b to refer a")
b = ctypes.cast(id(a), ctypes.py_object).value
print("b equals", b)
print("id(b):", id(b))
c = 130 + 7
print("id(c):", id(c))

def run():
    z = np.sin(1.37 * np.pi)
    print("\nz =", z)
    return z, id(z)

Z = run()
print("z =", Z[0])
print("inside method:", Z[1])
print("outside method:", id(Z[0]))
