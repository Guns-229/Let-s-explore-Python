# import time
import os


# import time
# class benchmark(object):

#     def __init__(self,code_name, verbose=False):
#         self.code_name = code_name
#         self.verbose = verbose

#     def __enter__(self):
#         self.start = time.time()
#         return self

#     def __exit__(self, *exc):
#         end = time.time()
#         self.time_taken = end - self.start
#         if self.verbose:
#             print(f"{self.code_name} : {(self.time_taken):0.7f} seconds")
#         return False


txt = open(os.path.join("data", "pg7864.txt")).read()
key = "Vedas do no allow killing of any live entity"

# original_time = []
# for _ in range(100):
#     with benchmark("Original") as b:


def xor_strings(s, t):
    """xor two strings together.

    URL: https://en.wikipedia.org/wiki/XOR_cipher.
    """
    if isinstance(s, str):
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        return bytes([a ^ b for a, b in zip(s, t)])


def update_key(key, length):
    return (key * (int(length / len(key)) + 1))[:length]


if len(txt) > len(key):
    key_new = update_key(key, len(txt))
else:
    key_new = key[len(txt)]

enc_txt = xor_strings(txt, key_new)
dec_txt =  xor_strings(enc_txt, key_new)
    # original_time.append(b.time_taken)


# from statistics import mean, median

# print("Mean: ", mean(original_time))
# print("Median: ", median(original_time))
