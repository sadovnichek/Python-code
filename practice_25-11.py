import struct
import os

filename = "file.txt"
size = os.path.getsize(filename)

with open(filename) as file:
    while size > 0:
        size -= 1
        file.seek(size)
        print(f'{file.read(1)}', end = '')

l = [1,3,5,7]

# > is big endian, 4 is count of values, i is type
pack_obj = struct.pack('>4i', l[0], l[1], l[2], l[3])

# print(pack_obj)

t = struct.unpack('>4i', pack_obj)

# print(t)
