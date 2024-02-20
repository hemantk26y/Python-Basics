""" WAP to check whether python shell executing in 32bit 64bit mode on OS """

import struct
print(struct.calcsize("P"*8))
