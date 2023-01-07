#LISTS
heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]

print(heights[2])  # 67
print(heights)  # entire list

#List could contain multiple types
ints_and_strings = [1, 2, 3, "four", "five", "ints_and_strings"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]

#list methods
example_list = [5, 5, 1, 2, 3, 4]

#Using Append
example_list.append(5)  # add 5 to the end of the list
print(example_list)

#conctenation of lists
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

my_list = [1, 2, 3]
one = my_list + [100]
print(one)

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders
print(orders_combined)

#Using Remove
example_list.remove(5)  # removes first 5
print(example_list)

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
order_list.remove("Flatbread")
print(order_list)

#2d remove
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
customer_data[1].remove(customer_data[1][2])  # removes Ben's False element
print(customer_data)

# delete item based on its position
del example_list[0]  # removes first item
print(example_list)

#accessing element by position
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
print(employees[6])

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1] #negative index goes from the back. -1 is the last element
print(last_element)

index5_element = shopping_list[5]
print(index5_element)

#modify the list
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
garden[2] = "Strawberries"  # replaces the third item on the list

print(garden)

# two-dimensional lists
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]

#Access the sublist at index 0, and then access the 1st index of that sublist.
noelles_height = heights[0][1]  # accessing second element of first item
print(noelles_height)  # 61

#example 1
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

#modification of 2d lists
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]

# The list of Jenny is at index 0. The hobby is at index 1.
class_name_hobbies[0][1] = "Meditation"  # this is replacement
print(class_name_hobbies)

# The list of Jenny is at index 0. The hobby is at index 1.
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)

#example 2
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# example 3
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

customer_data[2][2] = False

customer_data[1].remove(customer_data[1][2])

customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)

#  project Gradebook
print("\nProject Gradebook")

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subject = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88]
]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

gradebook[-1][-1] = 98
print(gradebook)

gradebook[2].remove(gradebook[2][1])
gradebook[2].append("Pass")  # append 2d list
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
