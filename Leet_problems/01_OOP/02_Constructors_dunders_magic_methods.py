"""
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet
"""

# __init__
"""
The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach. 
The __init__ function is called every time an object is created from a class. The __init__ method lets the class 
initialize the object's attributes and serves no other purpose. It is only used within classes.
"""
class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:
            # then shout it out
            print(phrase.upper())


shout1 = Shouter("shout") # prints "SHOUT"
shout2 = Shouter(2) # prints nothing as not a str
shout3 = Shouter("let it all out") # prints "LET IT ALL OUT"

# __repr__
"""
Python __repr__() function returns the object representation in string format. This method is called when repr() 
function is invoked on the object. If possible, the string returned should be a valid Python expression that can be 
used to reconstruct the object again
"""
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self): # can only have self as param, only returns strings
        return self.name


argus = Employee("Argus Filch")
print(argus)  # Without __repr__ it will show class and memory object

# Dir - lists all the attributes of an object
class FakeDict:
    pass


fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print(dir(fake_dict))

def this_function_is_an_object(number):
    number += 1
    return "hyj"

print(dir(this_function_is_an_object))