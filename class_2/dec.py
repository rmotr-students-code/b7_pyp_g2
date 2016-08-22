
def trace(f):
    # f == add
    def wrapped(*args, **kwargs):
        print("Invoking function %s" % f.__name__)
        res = f(*args, **kwargs)
        print("Result of %s was %s"  % (f.__name__, res))
        return res
    return wrapped


# @trace
def add(x, y):
    return x + y

add = trace(add)
print(add(2, 3))