def in_binary(number):
    array = []
    while number != 0:
        array.append(number % 2)
        number = number // 2
    return array


def in_decimal(array):
    k = 1
    result = 0
    for digit in array:
        if digit == 1:
            result += k
        k = k * 2
    return result


def xor(arr1, arr2):
    arr3 = []
    carry = 0
    for i in range(max(len(arr1), len(arr2))):
        if len(arr1) > i:
            num1 = arr1[i]
        else:
            num1 = 0
        if len(arr2) > i:
            num2 = arr2[i]
        else:
            num2 = 0
        number = num1 + num2 + carry
        if number == 3 or number == 1:
            arr3.append(1)
        else:
            arr3.append(0)
        if number >= 2:
            carry = 1
        else:
            carry = 0
    if carry == 1:
        arr3.append(1)
    return arr3


def multiply(big, small):
    array = [0]
    k = 0
    for i in small:
        arr2 = big
        if k != 0:
            arr2.insert(0, 0)
        if i == 1:
            array = xor(arr2, array)
        k += 1
    return array


def my_power(base, power):
    array = in_binary(base)

    for i in range(power - 1):
        array = multiply(array, in_binary(base))

    return in_decimal(array)


def my_pow(base, power, mod):
    result = 1
    curse = 0
    while mod > result and curse < power:
        result = result * base
        curse += 1
    if curse < power:
        return (my_pow(result % mod, power // curse, mod) * (base ** (power % curse))) % mod
    else:
        return base ** power
