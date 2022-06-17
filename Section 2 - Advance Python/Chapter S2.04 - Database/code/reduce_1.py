from functools import reduce


def countme(x):
    return x.count('the')

sentences = ['Copy the variable assignment for our new empty list'
             'Copy the expression that we’ve been append-ing into this new list'
             'Copy the for loop line, excluding the final'
             'Copy the if statement line, also without the']

sam_count = reduce(countme, sentences, 0)
print(sam_count)
