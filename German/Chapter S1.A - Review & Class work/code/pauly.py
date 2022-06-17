class A:
    def __str__(self):
        return("K.V. Pauly")

class B(A):
    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()

def main():
    a = A()
    b = B()
    c = C()
    print(a, b, c)


if __name__ == "__main__":
    main()
