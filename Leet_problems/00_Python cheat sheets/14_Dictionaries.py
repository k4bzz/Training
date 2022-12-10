# DICTIONARIES

"""
A dictionary is an unordered set of key: value pairs.

https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-dictionaries/cheatsheet
"""

menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# PRINT
my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])

# ASSIGN A NEW VALUE
my_dictionary["song"] = "Paradise City"
print(my_dictionary)

# ADDING A KEY
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

# UPDATE
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)

# OVERWRITE VALUES
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

# TODO learn zip
# ZIP

"""
The zip() function returns a zip object, which is an iterator of 
tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with 
the least items decides the length of the new iterator.
"""

a = ["John", "Charles", "Mike"]  # list
b = ["Jenny", "Christy", "Monica", "Vicky"]
c = ("1", "2", "3")  # tuple

x = zip(a, b, c)  # shortest list defines the length

print(x)  # will show the object location
print(list(x))  # will print as a list. Basically need to define the type, so it can be printed

# DICT COMPREHENSIONS
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)

# DICT EXAMPLE
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song:playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)


