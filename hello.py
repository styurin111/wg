# print('Hello World')


import random
import string


def generate_random_key(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

print(generate_random_key(44))