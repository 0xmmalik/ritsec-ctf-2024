# from Crypto.Random.random import getrandbits
from Crypto.Util import number
from server import oracle
from time import time
from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(10000)

bits = 32
p, q = 34913, 56437
e = 63997
n = p * q

input((p-1)*(q-1))

print(n)
d = pow(e, -1, (p - 1) * (q - 1))

flag = b'RC{b3etr007}'

c = f'{pow(int.from_bytes(flag[:4]), e, n)},{pow(int.from_bytes(flag[4:8]), e, n)},{pow(int.from_bytes(flag[8:12]), e, n)}'
c_parts = list(map(int, c.split(',')))
print(c_parts)
for part in c_parts:
    print(hex(pow(part, d, n)))

print(d)

raise SystemExit()
d_bits = list(map(int, bin(d)[-1:1:-1]))
times = []
diffs = [0]
for n in range(bits):
    s = time()
    print(oracle(150, d, 1000000000, n + 1).hex(), end=', ')
    times.append(time() - s)
    input(times[-1])

for i in range(1, len(times)):
    diffs.append(times[i] - times[i-1])

plt.subplot(2, 1, 1)
plt.plot(diffs)
plt.subplot(2, 1, 2)
plt.plot(d_bits)
plt.show()
