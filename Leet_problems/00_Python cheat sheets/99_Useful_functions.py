#CHECKS THE INPUT FOR ITS TYPE

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")


input1 = input("Enter your Age ")
check_user_input(input1)

input2 = input("Enter any number ")
check_user_input(input2)

input2 = input("Enter the last number ")
check_user_input(input2)


"""
25 tips for python
"""

import logging
import socket
import subprocess
import time
from collections import namedtuple

import numpy as np


# Manual vs F strings
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print("Wow " + name + "! you have " + str(subscribers) + " subscribers!")
    else:
        print("Lol " + name + " that's not many subs")

    # better
    if subscribers > 100000:
        print(f"Wow {name}! you have {subscribers} subscribers!")
    else:
        print(f"Lol {name} that's not many subs")


# Manual close file
def manually_calling_close_on_a_file(filename):
    f = open(filename, "w")
    f.write("hello!\n")
    f.close()

    with open(filename, "w") as f:
        f.write("hello!\n")
    # close automatic, even if exception

# TODO what is that?
def finally_instead_of_context_manager(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()

    # close even if exception
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')

# TODO what is that?
def bare_except():
    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except:  # oops! can't CTRL-C to exit
            print("Not a number, try again")

    while True:
        try:
            s = input("Input a number: ")
            x = int(s)
            break
        except Exception:  # still better to use ValueError
            print("Not a number, try again")


# TODO what is that?
def caret_and_exponentiation(x, p):
    y = x ^ p  # bitwise xor of x and p, not exponentiation
    y = x ** p

# TODO what is that?
def mutable_default_arguments():
    def append(n, l=[]):
        l.append(n)
        return l

    l1 = append(0)  # [0]
    l2 = append(1)  # [0, 1]

    def append(n, l=None):
        if l is None:
            l = []
        l.append(n)
        return l

    l1 = append(0)  # [0]
    l2 = append(1)  # [1]

# Comprehensions
def never_using_comprehensions():
    squares = {}
    for i in range(10):
        squares[i] = i * i

    # same
    odd_squares = {i: i * i for i in range(10)}

def always_using_comprehensions(a, b, n):
    """matrix product of a, b of length n x n"""
    c = [
        sum(a[n * i + k] * b[n * k + j] for k in range(n))
        for i in range(n)
        for j in range(n)
    ]

    c = []
    for i in range(n):
        for j in range(n):
            ij_entry = sum(a[n * i + k] * b[n * k + j] for k in range(n))
            c.append(ij_entry)

    return c

# TODO what is that?
def checking_type_equality():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)

    if type(p) == tuple:
        print("it's a tuple")
    else:
        print("it's not a tuple")

    # probably meant to check if is instance of tuple
    if isinstance(p, tuple):
        print("it's a tuple")
    else:
        print("it's not a tuple")

# TODO what is that?
def equality_for_singletons(x):
    if x == None:
        pass

    if x == True:
        pass

    if x == False:
        pass

    # better
    if x is None:
        pass

    if x is True:
        pass

    if x is False:
        pass

# CHECKING BOOL OR LEN
def checking_bool_or_len(x):
    if bool(x): # if true
        pass

    if len(x) != 0:
        pass

    # usually equivalent to
    if x:
        pass

# TODO to learn!
def range_len_pattern():
    a = [1, 2, 3]
    for i in range(len(a)):
        v = a[i]
        ...

    # instead
    for v in a:
        ...

    # or if you wanted the index
    for i, v in enumerate(a):
        print(f"index: {i}")  # prints Index
        print(f"value: {v}")  # prints Value

        """
        Enumerate return/yield generator as a result.
        Generator - value that can be used ONLY ONCE.
        First loop run writes a generator - every other re-writes it to a current value.
        Generators cant be used more that once.
        
        def enumerate(sequence, start=0):
            n = start
            for elem in sequence:
                yield n, elem
                n += 1
        
        """

        # string = "dog"
        # >> > print(list(enumerate(string)))
        # [(0, 'd'), (1, 'o'), (2, 'g')]

        ...

    # using i to sync between two things?
    b = [4, 5, 6]
    for i in range(len(b)):
        av = a[i]
        bv = b[i]
        ...

    # instead use zip
    for av, bv in zip(a, b):
        ...

# TODO to learn
def for_key_in_dict_keys():
    d = {"a": 1, "b": 2, "c": 3}
    for key in d.keys():
        ...

    # that's the default
    for key in d:
        ...

    # or if you meant to make a copy of keys
    for key in list():
        ...

#TODO what is that?
def not_using_dict_items():
    d = {"a": 1, "b": 2, "c": 3}
    for key in d:
        val = d[key]
        ...

    for key, val in d.items():
        ...

def tuple_unpacking():
    x = 0
    y = 1

    tmp = x
    x = y
    y = tmp

    x, y = 0, 1
    x, y = y, x

    mytuple = 1, 2
    x = mytuple[0]
    y = mytuple[1]

    x, y = mytuple


def index_counter_variable():
    l = [1, 2, 3]

    i = 0
    for x in l:
        ...
        i += 1

    for i, x in enumerate(l):
        ...

def timing_with_time():
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(end - start)

    # more accurate
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)



def print_vs_logging():
    print("debug info")
    print("just some info")
    print("bad error")

    # versus
    # in main
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)

    # wherever
    logging.debug("debug info")
    logging.info("just some info")
    logging.error("uh oh :(")

def subprocess_with_shell_true():
    subprocess.run(["ls -l"], capture_output=True, shell=True)

    subprocess.run(["ls", "-l"], capture_output=True)

def not_using_numpy_pandas():
    x = list(range(100))
    y = list(range(100))
    s = [a + b for a, b in zip(x, y)]

    # better (faster)
    x = np.arange(100)
    y = np.arange(100)
    s = x + y


def not_following_pep8():
    x = (1, 2)
    y=5
    l = [1,2,3]

    def func(x=5):
        ...


def python2_thinking():
    x = 10000000000000000000
    print(x in range(2 * x))  # ranges are lazy, this will be fast

    d = {"a": 1, "b": 2, "c": 3}
    keys = d.keys()
    del d["a"]
    print("a" in keys)  # keys is a "view", not a copy