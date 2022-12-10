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

students = {key: value for key, value in zip(names, heights)}
print(students)

# DICT EXAMPLE
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {song: playcount for song, playcount in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

# GET A VALUE BY KEY
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599,
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}

print(building_heights["Burj Khalifa"])  # get VALUE by KEY

# KEY THAT DOESNT EXIST
# print(building_heights["Landmark 81"])  # will throw the KeyError

key_to_check = "Landmark 81"

if key_to_check in building_heights:
    print(building_heights["Landmark 81"])  # will return FALSE

# SAFE WAY OF GETTING KEYS
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599,
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}

# this line will return 632:
print(building_heights.get("Shanghai Tower"))

# this line will return None:
print(building_heights.get("My House"))

# you can specify the result to return if the key doesnt exist
print(building_heights.get("My House", "XYJ"))

# DELETING A KEY
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace",
          298787: "Pasta Maker"}
print(raffle)

raffle.pop(320291, "No Prize")
print(raffle)

raffle.pop(10000, "No Prize")
print(raffle)

raffle.pop(412123, "No prize")
print(raffle)

# EXAMPLE
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

# GET ALL KEYS
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95],
               "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))  # you can print all KEYs as list
print(test_scores.keys())  # builtin function KEYS. Returns view only dict_keys object that you cant modify

for student in test_scores.keys():
    print(student)

# GET ALL VALUES
test_scores = {"Grace": [80, 72, 90], "Jeffrey": [88, 68, 81], "Sylvia": [80, 82, 84], "Pedro": [98, 96, 95],
               "Martin": [78, 80, 78], "Dina": [64, 60, 75]}

for score_list in test_scores.values():
    print(score_list)

list(test_scores.values())  # list of all VALUES
print(test_scores.values())

# EXAMPLE
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

total_exercises = 0

for i in num_exercises.values():
    total_exercises += i

print(total_exercises)

# GET ALL ITEMS
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
    print(f"KEY: {company} VALUE: {value}")
    # print(company + " has a value of " + str(value) + " billion dollars. ")

# EXERCISE
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor",
          5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit",
          10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance",
          15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement",
          21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13, 0)
spread["present"] = tarot.pop(22, 0)
spread["future"] = tarot.pop(10, 0)

for key, value in spread.items():
    print(f"Your {key} is the {value} card.")