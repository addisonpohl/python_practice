# Recursion example with factorials

def recursive_function(n):
    """ returns the factorial of the provided int using recursion:
        Ex: if 5 was provided as an argument 5*4*3*2*1 would be returned.
    """

    if n < 0:
        return - 1
    elif n < 2:
        return 1
    else:
        return n * recursive_function(n - 1)


print(recursive_function(5))
