def sum(a, b):
    try:
        return a + b
    except Exception as e:
        print("!!! Error !!!", e)
        breakpoint()

total = sum(10, a)
print(total)


