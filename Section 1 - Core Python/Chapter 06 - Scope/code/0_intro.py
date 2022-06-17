month = 7
year = 1947


def A():
    print("Entering A")
    month = 3
    date = 10
    print(f"{locals()=}")
    print(f"{globals()=}")
    print("Leaving A")


def B():
    print("Entering B")
    month = 2
    date = 15
    print(f"{locals()=}")
    print(f"{globals()=}")
    print("Leaving B")


A()
B()

print("*"*10)
print(f"{locals()=}")
print(f"{globals()=}")
