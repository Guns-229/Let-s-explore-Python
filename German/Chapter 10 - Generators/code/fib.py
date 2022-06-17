"""."""


def fib(n):
    """."""
    a, b = 0, 1
    for _ in range(n): # 0..9
        yield a
        a, b = b, a + b


num = 10
print(list(fib(num)))
# 0, 1, 1, 2, 3
