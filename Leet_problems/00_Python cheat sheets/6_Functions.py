#  FUNCTIONS

def directions_to_timesSq():  # function with no parameters
    print("Walk 4 mins to 34th St Herald Square train station")

directions_to_timesSq()  # calling out the function

#  intendation matters!
def weather_check():
    print("Looks great outside! Enjoy your trip.")  # printed second!
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")  # printed first!!

weather_check()

#  Function with parameters
def trip_welcome(destination):
    print("Welcome to Tripcademy!")
    print("Looks like you're going to " + destination + " today.")

trip_welcome("Times Square")

#  example 1
def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

#  Multiple parameters
def trip_welcome(origin, destination):
    print("Welcome to Tripcademy")
    print("Looks like you are traveling from " + origin)
    print("And you are heading to " + destination)

trip_welcome("Prospect Park", "Atlantic Terminal")

#  example 2
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print("Overall total is: " + str(hotel_total + car_rental_total + plane_ticket_price))  # need to str number

calculate_expenses(200, 100, 100, 5)

#  Types of arguments: Position
def calculate_taxi_price1(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount )
    # 100 is miles_to_travel
    # 10 is rate
    # 5 is discount
calculate_taxi_price1(100, 10, 5)

#  Types of arguments: Keyword
def calculate_taxi_price2(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount )

calculate_taxi_price2(rate=0.5, discount=10, miles_to_travel=100)  # doesnt matter the order

#  Types of arguments: Default
def calculate_taxi_price3(miles_to_travel, rate, discount = 10):
    print(miles_to_travel * rate - discount )

# Using the default value of 10 for discount.
calculate_taxi_price3(10, 0.5)  # keeps discount default

# Overwriting the default value of 10 with 20
calculate_taxi_price3(10, 0.5, 20)  # overwrites the discount

#  example 3
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")

trip_planner("Denmark", "France", "Germany")

trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

trip_planner("Brooklyn", "Queens")


#  Built in functions

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)


# Help for functions
help("string")

# example 3
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)  # max across provided
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)  # min across provided
print(min_price)

rounded_price = round(tshirt_price, 1)  # round to 1 decimal point
print(rounded_price)


# RETURN
def calculate_exchange_usd(us_dollars, exchange_rate):
    return us_dollars * exchange_rate


new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

# example 4
current_budget = 3500.75

def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
    return(budget - expense)  # returns value that can be then used in the code (out of function) if assiged to a variable

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)  # assigning to a variable
print_remaining_budget(new_budget_after_shirt)

# Multiple returns
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):  # takes list as input
    first_day = " Tomorrow the weather will be " + weather[0]
    second_day = " The following day it will be " + weather[1]
    third_day = " Two days from now it will be " + weather[2]
    return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)  # takes mon, tue, wed as return variables & weather_data as list for input

print(monday)
print(tuesday)
print(wednesday)

# example 6
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

trip_planner_welcome("Punk")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are travelling to " + destination)
  print("You will be travelling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("A", "B", estimate)

# PROJECT
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass, c=3*10**8):
    return mass * c**2

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

x = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(x) + " Joules of work over " + str(train_distance) + " meters.")
