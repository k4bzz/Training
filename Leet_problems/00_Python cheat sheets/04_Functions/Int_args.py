"""
https://www.codecademy.com/learn/learn-intermediate-python-3/modules/int-python-function-arguments/cheatsheet

Well, in Python, there is an additional operator called the unpacking operator (*).
The unpacking operator allows us to give our functions a variable number of arguments by performing what's
known as positional argument packing.
"""

# Example of print with number of args
print('This', 'is', 'the', 'print', 'function')


def my_function(*args):  # useful when you don't know the exact number of arguments coming. Like menu order
    print(args)


my_function('Arg1', 245, False)
