from functools import wraps


def register_gw_method(method_or_name):
    def decorator(method):
        if callable(method_or_name):
            method.gw_method = method.__name__
        else:
            method.gw_method = method_or_name

        @wraps(method)
        def wrapper(*args, **kwargs):
            print(")*")
            method(*args, **kwargs)
            print(*args, **kwargs)
        return wrapper
    if callable(method_or_name):
        return decorator(method_or_name)
    return decorator


@register_gw_method
def my_function():
    print('hi...')


@register_gw_method('say_hi')
def my_function_test():
    print('hi...')


my_function()

my_function_test()
