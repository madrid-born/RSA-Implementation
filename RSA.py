from BigPower import my_pow
import math
from GroupInverse import inverse
from BigPrime import prime
import random


class RSA:
    def __init__(self):
        p = prime()
        q = prime()
        n = p * q
        phi = (p-1) * (q-1)
        a = random.randint(1, phi)
        while math.gcd(a, phi) != 1:
            a = random.randint(1, phi)
        b = inverse(phi, a)
        self.pk = [b, n]
        self.sk = [a, n]

    def __call__(self, pk, sk):
        self.pk = pk
        self.sk = sk

    def Enc(self, message):
        c = my_pow(message, self.pk[0], self.pk[1])
        return c

    def Dec(self, message):
        m = my_pow(message, self.sk[0], self.sk[1])
        return m
