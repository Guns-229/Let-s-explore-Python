import string
from random import choice, randint


def get_rand_string(min_len=10, max_len=20):
    allchar = string.ascii_letters + string.punctuation + string.digits
    return "".join(choice(allchar)
                   for x in range(randint(min_len, max_len)))
