def only_numeric_arguments(integer, floats):
    def actual_decorator(f):
        def new_f(a, b):
            types_allowed = []
            if integer:
                types_allowed.append(int)
            if floats:
                types_allowed.append(float)
            if type(a) not in types_allowed or type(b) not in types_allowed:
                raise ValueError("Only int arguments allowed")
            return f(a, b)
        return new_f
    return actual_decorator


#@only_numeric_arguments(integer=True, floats=True)
def add(a, b):
    return a + b

add = only_numeric_arguments(integer=True, floats=True)(add)


print(add(9.0, 3))