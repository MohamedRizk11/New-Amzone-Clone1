import random


def genarate_code(lenght=8):
    data='123456789ABCDEFJHKLMNOPQ'
    Code=''.join(random.choice(data)for _ in range(lenght))
    return Code