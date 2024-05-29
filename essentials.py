from BigPower import in_binary
from BigPower import in_decimal


def normal_padding(number):
    array = in_binary(number)
    length = len(array)
    for i in range(256 - length):
        array.insert(0, 0)
    number = in_decimal(array)
    return number
