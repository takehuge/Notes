import struct
import numpy

# reading data sequentially
data = []
binaryFile = open("LabviewDAT", mode='rb')
# datas = binaryFile.read(8)
# i0 = datas.find(b'#')
# print(i0)
data = struct.unpack('>d', binaryFile.read(8))
print(data)
data = struct.unpack('>d', binaryFile.read(8))
print(data)

data = numpy.fromfile('LabviewDAT', dtype='>f')
print(data[19800:20000])