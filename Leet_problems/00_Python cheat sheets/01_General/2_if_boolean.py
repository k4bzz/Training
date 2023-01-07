# boolean & types
my_baby_bool = "true"
print(type(my_baby_bool))  # string

my_baby_bool_two = True
print(type(my_baby_bool_two))  # bool

# if statements
is_raining = True

if is_raining:  # ':' instead of Then
    print("bring an umbrella")

# relational operations
x = 20
y = 20
if x == y:
    print("These numbers are the same")

# AND
(1 + 1 == 2) and (2 + 2 == 4)  # True
(1 > 9) and (5 != 6)  # False
(1 + 1 == 2) and (2 < 1)  # False
(0 == 10) and (1 + 1 == 1)  # False

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
    print("You meet the requirements to graduate!")

# OR
True or (3 + 4 == 7)  # True
(1 - 1 == 0) or False  # True
(2 < 0) or True  # True
(3 == 8) or (3 > 4)  # False

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
    print("You have met at least one of the requirements.")

# NOT
not 1 + 1 == 2  # False
not 7 < 0  # True

credits = 120
gpa = 1.8

if not (credits >= 120):
    print("You do not have enough credits to graduate")

if not (gpa >= 2.0):
    print("Your GPA is not high enough to graduate")

if not (credits >= 120) and not (gpa >= 2.0):
    print("You do not meet either requirement to graduate!")

#IN
numbers = [1, 2, 3, 4]
2 in numbers # True. Code presented is for Terminal

#NOT IN
banned_users = ['lax', 'pidr']
user = 'onotole'

if user not in banned_users:
    print(f"{user.title()}, not banned lol")

# ElSE
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
    print("You meet the requirements to graduate!")
else:
    print("You do not meet the requirements to graduate.")

# ELSE IF / ELIF
grade = 86

if grade >= 90:
    print("A")
elif grade >= 80:  # B
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

if planet == 1:
    weight = weight * 0.91
elif planet == 2:
    weight = weight * 0.38
elif planet == 3:
    weight = weight * 2.34
elif planet == 4:
    weight = weight * 1.06
elif planet == 5:
    weight = weight * 0.92
elif planet == 6:
    weight = weight * 1.19

print("Your weight:", weight)

#Checking for equality
car = 'Audi'
car.lower() == 'audi' #will return True

# Project 1
import random

name = "Alex"
question = "Are you crazy?"
answer = ""

random_number = random.randint(1, 9)

# print(random_number)

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error"

if name == "":
    print('Question: %s' % question)
else:
    print('%s asks: %s' % (name, question))

if question == "":
    print("No question blyat")
else:
    print("Magic 8-Ball's answer: %s" % answer)

# Project 2
weight = 41.5

# Ground shipping
if weight <= 2:
   gs_cost = 1.5 * weight + 20
elif weight >2 and weight <= 6:
   gs_cost = 3 * weight + 20
elif weight >6 and weight <= 10:
   gs_cost = 4 * weight + 20
else:
   gs_cost = 4.75 * weight + 20

print('Ground shipping cost: $%f' % gs_cost)

#Ground Shipping Premium
gsp_cost = 125
print('Ground shipping premium: $%f' % gsp_cost)

# Drone shipping
if weight <= 2:
   ds_cost = 4.5 * weight
elif weight >2 and weight <= 6:
   ds_cost = 9 * weight
elif weight >6 and weight <= 10:
   ds_cost = 12 * weight
else:
   ds_cost = 14.25 * weight

print('Drone shipping cost: $%f' % ds_cost)

#IF works from first condition to the last
age = 2

if age < 100:
    print(f"check 100 worked. Age - {age}") # THIS WILL WORK, REST WON'T
elif age < 90:                              
    print(f"check 90 worked. Age - {age}")
else:                                       # ELSE BLOCK IS NOT REQUIRED, CAN BE OMITTED
    print(f"check ELSE worked. Age - {age}")