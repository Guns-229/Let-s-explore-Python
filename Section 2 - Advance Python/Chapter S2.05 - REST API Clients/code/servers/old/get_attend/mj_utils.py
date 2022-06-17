import string
import random

def rand_text(size=10, chars= string.punctuation +
                              string.digits +
                              string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    print(rand_text())
