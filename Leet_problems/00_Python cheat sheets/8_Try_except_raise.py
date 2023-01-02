# TRY/EXCEPT/ELSE/FINALLY

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# TRY/EXCEPT
try:
    print(w)
except:
    print("\nAn exception occurred")  # The try block will generate an exception, because w is not defined

# MANY EXCEPTIONS
try:
    print(w)
except NameError:
    print("\nVariable w is not defined")  # Print one message if the try block raises a NameError
    # and another for other errors
except:
    print("Something else went wrong")

# ELSE
try:
    print("\nHello")
except:
    print("Something went wrong")
else:  # You can use the else keyword to define a block of code to be executed if no errors were raised
    print("Nothing went wrong")  # In this example, the try block does not generate any error

# FINALLY
try:
    print(w)
except:
    print("\nSomething went wrong")
finally:  # The finally block, if specified, will be executed regardless if the try block raises an error or not.
    print("The 'try except' is finished\n")

# EXAMPLE
try:
    f = open("demofile.txt")  # try open
    try:
        f.write("Lorum Ipsum")  # if open try write
    except:
        print("Something went wrong when writing to the file")  # error writing
    finally:
        f.close()  # close if open
except:
    print("Something went wrong when opening the file")  # error

# RAISING exception
x = -1

# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

q = "hello"

# Wont throw an exception as code above already did. Only one exception can be thrown?
if not type(q) is int:
    raise TypeError("Only integers are allowed")

# EXAMPLE 2
key_to_check = "Landmark 81 v2"
try:
    print(building_heights[key_to_check])
except KeyError:
    print("That key doesn't exist!")

s = 'apple'

try:
    num = int(s)
except:
    raise
