"""
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-classes/cheatsheet
"""


# Classes

# Define Class
class Facade:
    pass


# Instantiate the instance of a class (object)
facade_1 = Facade()

# Check the type
facade_1_type = type(facade_1)
print(type(facade_1))


# Class variables
class Musician:
    title = "Rockstar"


drummer = Musician()
print(drummer.title)


# Methods
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))


pipi_pitbull = Dog()
pipi_pitbull.time_explanation()  # Prints "Dogs experience 7 years for every 1 human year."


# Methods with arguments
class DistanceConverter:
    kms_in_a_mile = 1.609

    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile


converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)  # prints "8.045"


# Simple example
class Circle:
    pi = 3.14

    # TODO static method?
    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(round_room_area)


# Getting attributes
class NoCustomAttributes:
    pass


attributeless = NoCustomAttributes()

try:
    attributeless.fake_attribute
except AttributeError:
    print("This text gets printed!")  # prints "This text gets printed!"

# hasattr returns true/false if attribute exists
hasattr(attributeless, "fake_attribute")  # returns False

# returns actual value of the attribute
getattr(attributeless, "other_fake_attribute", 800)  # returns 800, the default value


# Example
class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


p_grade = Grade(100)
pieter.add_grade(p_grade)
