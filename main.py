from BigPower import my_pow
from GroupInverse import inverse
from hashlib import sha256
import random
from BigPrime import prime
from RSA import RSA
from BlindSignature import BS

my_rsa = RSA()
bs = BS()
print(random.randint(0, 2))
key = [49347230176360267428677673276788099493590080554800992160147380993700686872973, 74606572546804832842741872800729068000383016121430476077477777510797594919679]
print((key[0] * key[1]) % 54607672546804832842741872800729068000383016121430476077477777510797594919679)
o, B = bs.blind(key)
sigma = bs.sign(B)
print(sigma)
small_sigma = bs.unblind(sigma, o)
print(small_sigma)
print(bs.verify(small_sigma, key))


'''message = int(input('enter : '))
enc = my_rsa.Enc(message)
print(enc)
print(my_rsa.Dec(enc))'''
'''print(my_pow(2, 1024))
print(inverse(75, 28))
print(sha256('hanieh'.encode()).hexdigest())'''

