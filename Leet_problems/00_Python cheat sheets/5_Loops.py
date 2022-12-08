#  LOOPS
#  https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-loops/cheatsheet

# YmH7Hj*iNX4JgpaN!GaQ
# noa@mitiga.io


ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

#  FOR loops
ingredients = ["milk2", "sugar2", "vanilla extract2", "dough2", "chocolate2"]
 
for ingredient in ingredients:
	print(ingredient)

#  one line FOR loops
for ingredient in ingredients: print(ingredient)

#  do something X number of times
for temp in range(6):  #  prints stuff 6 times with use of range
	print("Learning Loops!")

#  printing counter
for temp in range(6):
	print("Loop is on iteration number " + str(temp + 1))

#  WHILE loops
count = 0
while count <= 3:
	# Loop Body
	print(count)
	count += 1  
	# Any other code at this level of indentation will
	# run on each iteration

	#  ++ increases the integer by one and DOES NOT EXIST IN PYTHON 
	#  += increases the integer by the number of your choice

#  one line WHILE loop
count = 0
while count <= 3: print(count); count += 1  #  separate each statement with a ; to denote a separate line of code

#  example 1
#  While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
	# Loop Body
	# Print if the condition is still true
	print("Loop Iteration - count <= 3 is still true")
	# Print the current value of count 
	print("Count is currently " + str(count))
	# Increment count
	count += 1
	print(" ----- ")
print("While Loop ended")

#  WHILE loop for lists
ingredients2 = ["11", "22", "33", "44", "55"]

length = len(ingredients2)
index = 0
 
while index < length:
	print(ingredients2[index])
	index += 1


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
	print("I am learning about " + str(python_topics[index]))  # str is not necesarry in this cases
	index += 1

#  merge two lists with FOR loop
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
	students_period_B.append(student)
print(students_period_B)

#  Loop control Break
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
	print(item)
	if item == "knit dress":
		break
 
print("End of search!")

# example 2
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
	print(dog_breed)
	if dog_breed == dog_breed_I_want:
		print("They have the dog I want!")
		break


#  Loop control Continue
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
	if i <= 0:
		continue

		#  When our loop first encountered an element (-1) 
		#  that met the conditions of the if statement, 
		#  it checked the code inside the block and saw the continue. 
		#  When the loop then encounters a continue statement 
		#  it immediately skips the current iteration and moves onto
		#  the next element in the list (4).

	print(i)


#  nested Loops
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
	print(team)  # prints full sub lists in list

for team in project_teams:  # Loop through each sublist
	for student in team:  # Loop elements in each sublist
		print(student)

#  example 3

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
	print(location)
	for item in location:
		scoops_sold += item

print(scoops_sold)

#  List Comprehensions
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers] #  doubles items in the original list
print(doubled)

#  Comndition Comprehensions
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]  #  doubles only negatives
print(negative_doubled)  #  only prints negatives!

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]  # doubles negatives and triples positives
print(doubled)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [num for num in heights if num > 161]  #  num has to be lsited in brackets to get the value
print(can_ride_coaster)


# example 4
single_digits = list(range(10))
squares = []

for i in single_digits:
  print(single_digits[i])
  squares.append(single_digits[i]**2)  #  square each element and append to list squares

print(squares)

cubes = [num **3 for num in single_digits]  #  cube element via list comprehension

print(cubes)

#  Project Carly
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
	total_price += price

print("Total price: " + str(total_price))

average_price = total_price / len(prices)

print("Number of items: " + str(len(prices)))

print("Average Haircut Price: " + str(average_price))

new_prices = [haircut - 5 for haircut in prices]
print("Old prices: " + str(prices))
print("Prices -5:  " + str(new_prices))

total_revenue = 0

print(len(hairstyles))

for i in range(len(hairstyles)):  #  in XX has to be a range not an Int
	total_revenue += prices[i] * last_week[i]  #  incrementing by a specific expression

print(total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]  #  referencing items from multiple lists

print(cuts_under_30)