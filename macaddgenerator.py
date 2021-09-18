#/usr/bin/python
import random
mac = [random.choice(range(256)) for i in range(6)]
mac[0] |= 0x02
mac[0] &= 0xfe
s=":"
s=s.join('%02x' % m for m in mac)
print (s)
