"""
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet
"""

# __init__
class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:
            # then shout it out
            print(phrase.upper())


shout1 = Shouter("shout") # prints "SHOUT"
shout2 = Shouter(2) # prints nothing as not a str
shout3 = Shouter("let it all out") # prints "LET IT ALL OUT"