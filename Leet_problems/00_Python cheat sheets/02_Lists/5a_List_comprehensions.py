#  List Comprehensions
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers] #  doubles items in the original list
print(doubled)

#  Condition Comprehensions
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