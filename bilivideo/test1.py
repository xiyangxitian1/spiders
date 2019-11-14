import time
import math
import sys
from itertools import chain

# l = str(time.time()).replace('.', '')
# print(l)
# print(sys.maxsize)
# print(math.pow(sys.maxsize, 3))

c = chain(range(1000000))
# print(list(c))

s1 = time.time()
for i in chain(range(100000000)):
    a = 2
    b = 3
    c = a + b + i


s2 = time.time()
print(s2-s1)
s1 = time.time()
for i in range(100000000):
    a = 2
    b = 3
    c = a + b + i
s2 = time.time()
print(s2-s1)
