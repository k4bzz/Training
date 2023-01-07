# just print
x = "xyj"
print(x, "\n")

# print with new line
word = "xxx yyy"
print('STEP 2: ' + 'first string', word, '\n')

#multiple assignment
a, b, c = 0, 0, 0

#constants
MAX_CONST = 10 #python treats variables with all capitals as constants

# print with no space
number = 13
area = 1
print('STEP 3: ''string "%d"' % number)
print("The circle area is ", area)

#numbers with underscores
age_one = 10_000_000
print(age_one)

# 2 to the 10th power, or 1024
print(2 ** 10)

# 8 squared, or 64
print(8 ** 2)

# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)

#string concat
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
print(full_text)

# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# insert spaces
full_text = greeting_text + " " + question_text

# Prints "Hey there! How are you doing?"
print(full_text)

# Concatenating an integer with strings is possible if we turn the integer into a string first
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If we just want to print an integer
# we can pass a variable as an argument to
# print() regardless of whether
# it is a string.

# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

# First we have a variable with a number saved
number_of_miles_hiked = 12

# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2

# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14

hike_caption = "What an amazing time to walk through nature!"

# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
print(hike_caption)

#multi line strings
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
print(leaves_of_grass)

#test 1 in CA
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += "Item 1: " + lovely_loveseat_description + "\n"

customer_one_total += luxurious_lamp_price
customer_one_itemization += "Item 2: " + luxurious_lamp_description + "\n"

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print('Customer One Items:\n' '%s' % customer_one_itemization)
print('Customer One Total:\n' '%f' % customer_one_total) #slightly rounded float value
print(customer_one_total) #different float value

#user input with prompt
likes_snakes = input("Do you like snakes? ")
print(likes_snakes)

#user intput with no prompt
likes_snakes2 = input()
print(likes_snakes2)

print("Im from macbook!")