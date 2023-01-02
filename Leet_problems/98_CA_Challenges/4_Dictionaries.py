# Sum values of a dictionary
def sum_values(my_dictionary: dict) -> int:
    total = 0

    for number in my_dictionary:
        total += my_dictionary[number]
    return total

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

"""
CA Solution

def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total
"""

# Sum even keys
def sum_even_keys(my_dictionary: dict) -> int:
    total = 0

    for key in my_dictionary:
        if key % 2 == 0:
            total += my_dictionary[key]
    return total

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

"""
CA Solution

def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary.keys():
        if key%2 == 0:
            total += my_dictionary[key]
    return total
"""

# Add ten
def add_ten(my_dictionary: dict ) -> dict:
    dictionary = my_dictionary
    for key in my_dictionary:
        dictionary[key] += 10
    return dictionary

print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

# Values that are keys
def values_that_are_keys(my_dictionary: dict) -> list:
    new_list = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            new_list.append(value)
    return new_list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

# Max value
def max_key(my_dictionary: dict) -> int:
    max_val = float("-inf")
    max_key = float("-inf")

    for key, value in my_dictionary.items():
        if value > max_val:
            max_val = value
            max_key = key
    return max_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

"""
CA Solution

def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
"""