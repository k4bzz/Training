#  Advanced lists. Adding by Index. INSERT
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
store_line.insert(2, "Vikor")  # inserts into index 2 everything else moves to right
print(store_line)

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0, "Pineapple")
print(front_display_list)

#  remove by index: pop
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element = cs_topics.pop()  # .pop() removes last element if not provided with index. It stores removed element
print(cs_topics)
print(removed_element)

cs_topics.pop(2)
print(cs_topics)

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

data_science_topics.pop()
print(data_science_topics)
data_science_topics.pop(3)
print(data_science_topics)

# consecutive lists: range
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_range = range(10)
print(my_range)

print(list(my_range))

print(list(range(8)))

#  range starting at another number
my_list = range(2, 9)
print(list(my_list))

my_range2 = range(2, 9, 2)  # skips each number by 2
print(list(my_range2))

my_range3 = range(1, 100, 10)
print(list(my_range3))

# length
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len)

big_range = range(2, 3000, 10)
big_range_length = len(big_range)
print(big_range_length)

# slicing (parts of the list)
letters = ["a", "b", "c", "d", "e", "f", "g"]
sliced_list = letters[1:6]  # start 1-included end 6-excluded element
print(sliced_list)

# slicing - start and end of the lists
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3])  # print start to element 3

print(fruits[-2:])  # end of list

print(fruits[:-1])  # all but last element

#  counting in a list (how many times element occurs in a list)
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")  # how many times item "i" occurs
print(num_i)

number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])  # counts in 2d lists
print(num_pairs)

# sorting lists
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()  # alphabetial order
print(names)

names.sort(reverse=True)  # reverse sort
print(names)

x = names.sort()  # sort method doesnt provide value. It assigns "None" if assigned. SORTED function does
print(x)

#  sorting with SORTED
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names)  # SORTED generates new list
print(sorted_names)
print(names)  # original list remains the same

# project
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]

inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")

inventory.sort()

print(inventory)

#  project 2
toppings = ["pepperoni", "pineapple", "chees", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print('We sell %d different kinds of pizza!' % num_pizzas)

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

pizza_and_prices.pop(-1)
print(pizza_and_prices)

pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)

# combine lists with zip
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)  # This zip object contains the location of this variable in our computer’s memory. Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

print(names_and_heights)

converted_list = list(names_and_heights)
print(converted_list)  # sublists are tuples ()

#Copy list through slicing
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:] # that copies a list into a new one and keeps two separate

my_foods.append('1')
friends_foods.append('2')

print(my_foods) # ... 1
print(friends_foods) # ... 2

my_foods = friends_foods # will link one list to another and when added to one will appear in another

print(my_foods) # ... 2
print(friends_foods) # ... 2

#Checking if list is not empty
toppings = []

if toppings:
	for topping in toppings:		#This will return False if list has no items
		print(f"Adding {topping}")
	print("\nFinished")
else:
	print("Empty topping list")

#Checking across multiple lists
availavle_toppings = [1, 2, 3, 4, 5]
requested_toppings = [1, 2, 6]

for requested_topping in requested_toppings:
	if requested_topping in availavle_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we dont have {requested_topping}.")

print("\nFinished!")

# Built in count method that returns number of occurrences in the list
fruits = ['apple', 'banana', 'cherry', 'cherry']

x = fruits.count("cherry")
print(x) # 2

# Prints every other letter
s = "1234567890"
print(s[::2])