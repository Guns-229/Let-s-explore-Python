import os
from itertools import cycle
from memory_profiler import profile

txt = open(os.path.join("data", "pg7864.txt")).read()


key = [86, 101, 100, 97, 115, 32, 100, 111, 32, 110, 111, 32, 97, 108,
       108, 111, 119, 32, 107, 105, 108, 108, 105, 110, 103, 32, 111,
       102, 32, 97, 110, 121, 32, 108, 105, 118, 101, 32, 101,
       110, 116, 105, 116, 121]

@profile
def xor_strings(txt, key):
    return "".join(chr(ord(a) ^ b) for a, b in zip(txt, key))


@profile
def update_key(key, length):
    if len(txt) > len(key):
        return cycle(key)
    else:
        return key[len(txt)]


key_new = update_key(key, len(txt))
enc_txt = xor_strings(txt, key_new)
key_new = update_key(key, len(txt))
dec_txt = xor_strings(enc_txt, key_new)

# print(enc_txt[:200])
# print("".join(dec_txt[:200]))
