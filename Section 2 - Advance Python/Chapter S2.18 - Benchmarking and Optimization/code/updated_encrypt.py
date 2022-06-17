import os


txt = open(os.path.join("data", "pg7864.txt")).read()


key = [86, 101, 100, 97, 115, 32, 100, 111, 32, 110, 111, 32, 97, 108,
       108, 111, 119, 32, 107, 105, 108, 108, 105, 110, 103, 32, 111,
       102, 32, 97, 110, 121, 32, 108, 105, 118, 101, 32, 101,
       110, 116, 105, 116, 121]


def xor_strings_new(s, t):
    """xor two strings together.

    URL: https://en.wikipedia.org/wiki/XOR_cipher.
    """
    if isinstance(s, str):
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t))
    else:
        return bytes([a ^ b for a, b in zip(s, t)])


def update_key(key, length):
    return (key * (int(length / len(key)) + 1))[:length]


if len(txt) > len(key):
    key_new = update_key(key, len(txt))
else:
    key_new = key[len(txt)]

enc_txt = xor_strings_new(txt, key_new)
dec_txt = xor_strings_new(enc_txt, key_new)
# print(enc_txt[:200])
# print(dec_txt[:200])
