func_table = {}

def count_args(args):
    return len(args)

def overload(*args):
    def wrapper(func):
        func_table[count_args(args)]=func
        def call_func(*args):
            return func_table[count_args(args)](*args)
        return call_func
    return wrapper
    
    
@overload(int, int)
def func(x, y):
    return x+y

@overload(int, int, int)
def func(x, y, z):
    return x+y+z