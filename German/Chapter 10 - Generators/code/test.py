def gen_pares():
    """
    Generates even numbers from 0 to 20
    """
    i = 0


    yield i
    print("dada")
    i += 2
    yield i

# Shows each number and goes to the next
print(list(gen_pares()))
print(list(gen_pares()))
