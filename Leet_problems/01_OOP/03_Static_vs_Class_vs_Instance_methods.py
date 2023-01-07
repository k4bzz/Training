# coding=unicode_escape

# HAD TO DECLARE ENCODING DUE TO ' SIGNS (UTF-8 DOESN'T LIKE THEM)
"""
https://realpython.com/instance-class-and-static-methods-demystified/#:~:text=Class%20methods%20don't%20need,belong%20to%20the%20class's%20namespace.


Instance methods need a class instance and can access the instance through self.

Class methods don’t need a class instance. They can’t access the instance (self) but they have access
to the class itself via cls.

Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

Static and class methods communicate and (to a certain degree) enforce developer intent about class design.
This can have maintenance benefits.
"""

import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    """
    Instance method - Takes self as an argument. Not only can they modify object state, instance methods can also access 
    the class itself through the self.__class__ attribute. This means instance methods can also modify class state.
    """
    def area(self):
        return self.circle_area(self.radius)

    """
    Static method - Takes neither self nor cls arguments. Therefore a static method can neither modify object state 
    nor class state. Static methods are restricted in what data they can access - and they’re primarily a way
    to namespace your methods.
    """
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


    """
    Class method - Takes cls argument. Because the class method only has access to this cls argument, 
    it can’t modify object instance state. That would require access to self. However, class methods 
    can still modify class state that applies across all instances of the class.
    """
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])