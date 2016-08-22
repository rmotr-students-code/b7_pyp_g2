class only_numeric_arguments(object):
    def __init__(self, integer, floats):
        self.integer = integer
        self.floats = floats

    def __call__(self, f):
        def new_f(a, b):
            print("Executing %s" % f.__name__)
            return f(a, b)
        return new_f


@only_numeric_arguments(integer=True, floats=True)
def add(a, b):
    if type(a) != int or type(b) != int:
        raise
    return a + b
    


print(add(2, 3))