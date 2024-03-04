from random import randint
from time import sleep, time

import Crypto
from Crypto.Cipher import AES


def powr(b, e, m):
    if e == 0: return 1
    if e == 1: return b % m

    result = powr(b, e // 2, m)
    result = result * result
    sleep(0.1)
    if e % 2 == 1:
        result *= b
        sleep(0.1)

    return result % m


def oracle(b, n):
    e = 1700258389
    m = 1970384981

    r = powr(b, e % (2 ** n), m)

    aes = AES.new(b'matron_of_joseph', AES.MODE_CBC)
    return aes.encrypt(r.to_bytes(16))


if __name__ == '__main__':
    key = input("API Key: ")
    if key != "abadbd796f1b2ae8bd82e1195ad12373":
        print("Invalid API Key")
        raise SystemExit()
    while True:
        b = int(input("Base: "))
        n = int(input("Slice: "))
        print(oracle(b, n).hex())
