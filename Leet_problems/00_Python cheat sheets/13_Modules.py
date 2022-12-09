# MODULES

# RANDOM
import random

random_list = [random.randint(1, 100) for num in range(101)] #populates empty list with random number in range
print(random_list)

randomer_number = random.choice(random_list)  #random choice takes list and picks random item
print(randomer_number)

# RANDOM SAMPLE
nums = [1, 2, 3, 4, 5]
sample_nums = random.sample(nums, 3)  # random.sample takes a list and randomly selects k items from it
print(sample_nums)

# IMPORT ALIASES
from matplotlib import pyplot as plt

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

print(numbers_b)

plt.plot(numbers_a, numbers_b)

plt.show()

# DECIMALS
cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction) # Returns 0.44999999999999996

from decimal import Decimal

cost_of_gum = Decimal('0.1')  # will print out 2 digit after "." as 0.35 has two
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop # Returns 0.45 instead of 0.44999999999999996
print(cost_of_transaction)

four_decimal_points = 0.53 * 0.65
print(four_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('20.65')
print(four_decimal_points)

# IMPORTING FROM FILES
"""
same as with func/modules

File 1 - fileone.py
def always_three():
    return 3

File 2 - filetwo.py
from fileone import always_three

always_three()    
"""

# DATETIME
from datetime import datetime

birthday = datetime(1994, 2, 15, 4, 25, 12)
print(birthday)
print(birthday.year)
print(birthday.weekday())  # what day in a week that was

print(datetime.now())

print((datetime(2018, 1, 1) - datetime(2017, 1, 1)))

# STRPTIME -> datetime from a string
date = "Jan 15, 2011"

parsed_date = datetime.strptime(date,"%b %d, %Y")  # second argument is format into which to produce. Arguments are in python docs
print(parsed_date.month)

# STRFTIME -> string from a datetime
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print(date_string)

