from pdb import set_trace


def sum(a, b):
    try:
        return a + b
    except Exception as e:
        print("!!! Error !!!", e)
        set_trace()

a = "Aryan"

sum(10, a)
