import random
from BigPower import my_pow
from GroupInverse import inverse


class BS:
    def __init__(self):
        self.pk = [49347230176360267428677673276788099493590080554800992160147380993700686872973, 54607672546804832842741872800729068000383016121430476077477777510797594919679]
        self.sk = [20328680424282920420513649692109970224871396156148924435107437223606299827077, 54607672546804832842741872800729068000383016121430476077477777510797594919679]

    def blind(self, key):
        message = (key[0] * key[1]) % self.pk[1]
        o = random.randint(1, self.pk[1])
        B = message * my_pow(o, self.pk[0], self.pk[1])
        return o, B

    def sign(self, B):
        sigma = my_pow(B, self.sk[0], self.sk[1])
        return sigma

    def verify(self, sigma, key):
        message = (key[0] * key[1]) % self.pk[1]
        m = my_pow(sigma, self.pk[0], self.pk[1])
        if m == message:
            return True
        else:
            return False

    def unblind(self, sigma, o):
        varoon = inverse(self.pk[1], o)
        small_sigma = (sigma * varoon) % self.pk[1]
        return small_sigma
