"""."""

if __name__ == "__main__":
    a_name = b_name = 'Amit Shrivastava'
    print(a_name is b_name)
    print(a_name == b_name)

    a_name = 'Atul Shrivastava'
    b_name = [
        'A', 'm', 'i', 't', ' ', 'S', 'h', 'r', 'i', 'v', 'a', 's', 't', 'a',
        'v', 'a'
    ]
    print(a_name is "".join(b_name))
    print(a_name == "".join(b_name))
