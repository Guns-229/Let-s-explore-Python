class A:
    def __str__(self):
        return("K.V. Pauly")

class B(A):
    pass

class C(B):
    pass

def main():
    a = A()
    b = B()
    c = C()
    print(a, b, c)


if __name__ == "__main__":
    main()
