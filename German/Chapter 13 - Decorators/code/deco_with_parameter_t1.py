from functools import wraps

# def decorator(*deco_args, **deco_kwargs):
#     def real_decorator(func):
#         def inner(*args, **kwargs):
#             print(deco_args)
#             for k, v in deco_kwargs.items():
#                 print(k, v)
#             func(*args, **kwargs)
#         return inner
#     return real_decorator


def decorator(*deco_args, **deco_kwargs):
    def real_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(deco_args)
            for k, v in deco_kwargs.items():
                print(k, v)
            func(*args, **kwargs)
        return inner
    return real_decorator


@decorator("arg1", "arg2", test="dummy argument")
def print_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)


print_args(1, 2, 3, d="Satyam")
