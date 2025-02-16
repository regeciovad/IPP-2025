def create(n):
    def adder(x):
        return x + n
    return adder

add_one = create(1)

def foo(a=1, b=2):
    return a + b

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

# Variable-length arguments, including keyword arguments:
def spam(*args, **kwargs):
    print(args, kwargs)
