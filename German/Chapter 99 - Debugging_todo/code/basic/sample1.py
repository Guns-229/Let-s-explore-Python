import mox


def divide(a, b):
    return a / b


def ve_msg(err_msg, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        raise StandardError("Failed to get an exception in %s()"
                            % func.__name__)
    except Exception as e:
        if err_msg not in str(e):
            print(">%s< not match >%s<" % (err_msg, str(e)))


ve_msg("test", divide, 10, 10)
ve_msg("test", divide, 10, 0)

