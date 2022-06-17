def quest(x):
    x[0] = x[0] + “ Johri”
    x[1] = x[1] + “ Gupta”
    return id(x)
q = [“mayank”, “Manish”]
print(id(q) == quest(q))
