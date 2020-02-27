import random

def generator(length = 15):
    symbols = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = []
    for i in range(length):
        password.append(random.choice(symbols))
    return ''.join(password)


print(generator(10))