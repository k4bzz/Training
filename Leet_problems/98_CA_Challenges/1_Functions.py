#  Basic
#  lARGE POWER
print("Challenge 1")
def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False

print(large_power(2, 13))  # should print True
print(large_power(2, 12), str("\n"))  # should print False


#  OVER BUDGET
print("Challenge 2")
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    cost = [food_bill, electricity_bill, internet_bill, rent]
    #  print(sum(cost), budget)
    if budget < sum(cost):
        return True
    else:
        return False

print(over_budget(100, 20, 30, 10, 40))  # should print False
print(over_budget(80, 20, 30, 10, 30), str("\n"))  # should print True

#  TWICE AS LARGE
print("Challenge 3")

def twice_as_large(num1, num2):
    #if num1 / num2 > 2:   DIVISION
    if num1 > 2 * num2:  # MULTIPLICATION
        return True
    else:
        return False

print(twice_as_large(10, 5))  # should print False
print(twice_as_large(11, 5), str("\n"))  # should print True

#  DIVISION BY 10
print("Challenge 4")

def divisible_by_ten(num):
    if (num % 10 == 0):
        return True
    else:
        return False


print(divisible_by_ten(20))  # should print True
print(divisible_by_ten(25), str("\n"))  # should print False

#  NOT SUM TO TEN
print("Challenge 5")

def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False

print(not_sum_to_ten(9, -1))  # should print True
print(not_sum_to_ten(9, 1))  # should print False
print(not_sum_to_ten(5,5), str("\n"))  # should print False

#  Logical
#  IN RANGE
print("Challenge 2.1")

def in_range(num, lower, upper):
    if (num >= lower and num <= upper):
        return True
    return False  # no ELSE

print(in_range(10, 10, 10))  # should print True
print(in_range(5, 10, 20), str("\n"))  # should print False

#  SAME NAME
print("Challenge 2.2")

def same_name(your_name, my_name):
    if (your_name == my_name):
        return True
    return False

print(same_name("Colby", "Colby"))  # should print True
print(same_name("Tina", "Amber"), str("\n"))  # should print False

#  ALWAYS FALSE
print("Challenge 2.3")

def always_false(num):
    if num > num:
        return True
    return False

print(always_false(0))  # should print False
print(always_false(-1))  # should print False
print(always_false(1), str("\n"))  # should print False

#  COMPARISON / IN BETWEEN
print("Challenge 2.4")

def movie_review(rating):
    if (rating <= 5):
        return "Avoid at all costs!"
    elif (rating > 5 and rating < 9):
        return "This one was fun."
    else:
        return "Outstanding!"

print(movie_review(9))  # should print "Outstanding!"
print(movie_review(4))  # should print "Avoid at all costs!"
print(movie_review(6), str("\n"))  # should print "This one was fun."

#  MAX NUMBER
print("Challenge 2.5")

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

print(max_num(-10, 0, 10))  # should print 10
print(max_num(-10, 5, -30))  # should print 5
print(max_num(-5, -10, -10))  # should print -5
print(max_num(2, 3, 3), str("\n"))  # should print "It's a tie!"

#  Lists
#  APPEND LIST SIZE OT THE END
print("Challenge 3.1")

def append_size(lst):
    lst.append(len(lst))
    return lst

print(append_size([23, 42, 108]), str("\n"))

#  APPEND SUM OF ELEMENTS
print("Challenge 3.2")

def append_sum(lst):
    for i in range(3):
        sum = lst[-1]+lst[-2]
        lst.append(sum)
    return lst

print(append_sum([1, 1, 2]), str("\n"))

#  LIST LEN COMPARISON
print("Challenge 3.3")

def larger_list(lst1, lst2):
    if len(lst2) > len(lst1):
        return lst2[-1]
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]), str("\n"))

#  LIST LEN GREATER THAN X
print("Challenge 3.4")

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3), str("\n"))

#  MERGE LISTS AND SORT
print("Challenge 3.5")

def combine_sort(lst1, lst2):
    merged = lst1 + lst2
    merged.sort()
    return merged

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]), str("\n"))

#  Lists Advanced
#  EVERY THIRD NUMBER
print("Challenge 4.1")

def every_three_nums(start):
    return list(range(start, 101, 3))

    # third = []
    # if start <= 100:
    #     third = range(start, 101, 3)
    #     return list(third)
    # else:
    #     return third

print(every_three_nums(91), str("\n"))

#  REMOVE MIDDLE
print("Challenge 4.2")

def remove_middle(lst, start, end):
   return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3), str("\n"))

#  MORE FREQUENT NUMBER
print("Challenge 4.3")

def more_frequent_item(lst, item1, item2):
    if lst.count(item2) > lst.count(item1):
        return item2
    return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3), str("\n"))

#  DOUBLE THE ELEMENT AT INDEX
print("Challenge 4.4")

def double_index(lst, index):
    # Option 1 - changes input list
    # if index <= len(lst):
    #     lst[index] = lst[index]*2
    # return lst

    # Option 2 - creates new list
    # Checks to see if index is too big
    if index >= len(lst):
        return lst
    else:
        # Gets the original list up to index
        new_lst = lst[0:index]
    # Adds double the value at index to the new list
    new_lst.append(lst[index] * 2)
    #  Adds the rest of the original list
    new_lst = new_lst + lst[index + 1:]
    return new_lst

print(double_index([1, 2, 3, 4], 2))
print(double_index([3, 8, -10, 12], 2), str("\n"))

#  MIDDLE ITEM
print("Challenge 4.5")

def middle_element(lst):
    # Option from CA
    # def middle_element(lst):
    #     if len(lst) % 2 == 0:
    #         sum = lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]
    #         return sum / 2
    #     else:
    #         return lst[int(len(lst) / 2)]

    # print(len(lst))  # len 6
    # print(lst[len(lst)-1])  # last item is 5th
    # print(lst[(len(lst)  // 2) - 1])  # -10
    # print(lst[len(lst) // 2] + lst[len(lst)-1])
    # print(len(lst) / 2)  # division returns FLOAT!!!!
    # print(int(6*0.5))  # you cant turn it into INT
    # print(6//2)  # Floor division returns INT

    if len(lst) % 2 == 0:
        average = (lst[(len(lst)  // 2) - 1] + lst[(len(lst)  // 2)]) / 2
        return average
    else:
        average = lst[(len(lst)  // 2)]
    return average

print(middle_element([5, 2, -10, -4, 4, 5]), str("\n"))

#  Loops
#  DIVISION BY TEN
print("Challenge 5.1")

def divisible_by_ten(nums):
    count = 0
    for i in nums:  # represents item on the list (value) First i will be 20
        if (i % 10 == 0):
            count += 1
    return count

print(divisible_by_ten([20, 25, 30, 35, 40]), str("\n"))

#  CONCAT THE LISTS LOOP
print("Challenge 5.2")

def add_greetings(names):
    greetings = []
    for i in names:
        greetings.append("Hello, " + i)
    return greetings

print(add_greetings(["Owen", "Max", "Sophie"]), str("\n"))

#  DELETE STARTING EVEN NUMBERS
print("Challenge 5.3")

#def delete_starting_evens(lst):
    # MY SOLUTION
    # length = len(lst)
    # index = -1
    # cut = -1
    # new = []
    #
    # while index < length:
    #     if lst[index] % 2 == 0:
    #         cut += 1
    #     index +=1
    # new = lst[cut:]
    # return new

def delete_starting_evens(lst):  # CA SOLUTION
    while (len(lst) > 0 and lst[0] % 2 == 0):
        #print(lst[0])
        lst = lst[1:]  # shortens the list by 1 item from left
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([2, 8, 10]), str("\n"))

#  ODD INDEX NEW LIST
print("Challenge 5.4")

def odd_indices(lst):
    # MY SOLUTION
    # length = len(lst)
    # index = 0
    # odd = []
    #
    # while index < length:
    #     if index % 2 == 1:
    #         odd.append(lst[index])
    #     index += 1
    # return odd

    new_lst = []  # CA SOLUTION
    for index in range(1, len(lst), 2):  # range starts with ODD for the len of the list with step 2 (only odds)
        new_lst.append(lst[index])
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]), str("\n"))

#  EXPONENTS
print("Challenge 5.5")

def exponents(bases, powers):
    # Option 1
    new = [b ** p for b in bases for p in powers]

    # Option 2
    # for b in bases:
    #     for p in powers:
    #         new.append(b**p)
    return new
print(exponents([2, 3, 4], [1, 2, 3]), str("\n"))

#  ADVANCED LOOPS
#  LARGER SUM OF ELEMENTS OF LIST
print("Challenge 6.1")

def larger_sum(lst1, lst2):
    if sum(lst2) > sum(lst1):
        return lst2
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]), str("\n"))

#  SUM OF ELEMENTS IN THE LIST GREATER CERTAIN AMOUNT
print("Challenge 6.2")

def over_nine_thousand(lst):
    # if len(lst) > 0:
    #     total = 0
    #     i = 0
    #     while total < 9000 and i < len(lst):
    #         total += lst[i]
    #         i += 1
    #     return total
    # return 0

    # CA solution
    sum = 0
    for number in lst:
        sum += number
        if (sum > 9000):
            break
    return sum
print(over_nine_thousand([8000, 900, 120, 5000]), str("\n"))

#  MAX NUM
print("Challenge 6.3")

def max_num(num):
    # return max(num)       # too easy
    # max_i = float('-inf') # absolute minimum
    max_i = num[0]  # easier option
    for i in num:
        if i > max_i:
            max_i = i
    return max_i

print(max_num([50, -10, 0, 75, 20]), str("\n"))

#  SAME VALUES
print("Challenge 6.4")

def same_values(lst1, lst2):
    same = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            same.append(i)
    return same

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]), str("\n"))

#  REVERSED LIST
print("Challenge 6.5")

def reversed_list(lst1, lst2):
    # CA solution
    # for index in range(len(lst1)):
    #     if lst1[index] != lst2[len(lst2) - 1 - index]:
    #         return False
    # return True

    reversed = []
    for i in lst2:
        reversed.insert(0, i)  # inserts into index 2 everything else moves to right
    if lst1 == reversed:
        return True
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]), str("\n"))

#  FUNCTIONS
#  10th POWER
print("Challenge 7.1")

def tenth_power(num):
    return num ** 10

print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2), str("\n"))

#  SQUARE ROOT
print("Challenge 7.2")

def square_root(num):
    return num ** 0.5

print(square_root(16))
print(square_root(100), str("\n"))

#  PERCENTACE
print("Challenge 7.3")

def win_percentage(wins, losses):
    percentage = wins / (wins + losses) * 100
    return percentage

print(win_percentage(5, 5))
print(win_percentage(10, 0), str("\n"))

#  AVERAGE OF TWO
print("Challenge 7.4")

def average(num1, num2):
    average = (num1 + num2) / 2
    return average

print(average(1, 100))
print(average(1, -1), str("\n"))

#  REMAINDER
print("Challenge 7.5")

def remainder(num1, num2):
    rem = (num1 * 2) % (num2 / 2)
    return rem

print(remainder(15, 14))
print(remainder(9, 6), str("\n"))

#  FUNCTIONS ADVANCED
#  FIRST THREE MULTIPLES
print("Challenge 8.1")

def first_three_multiples(num):
    for i in range(1, 3):
        print(num * i)
    return num * 3

first_three_multiples(10)
first_three_multiples(0)

#  TIP PERCENTAGE
print("Challenge 8.2")

def tip(total, percentage):
    amount = total * (percentage / 100)
    return amount

print(tip(10, 25))
print(tip(0, 100), str("\n"))

#  PRINT NAME
print("Challenge 8.3")

def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"), str("\n"))

#  PRINT NAME
print("Challenge 8.4")

def dog_years(name, age):
    return name+", you are "+str(age * 7)+" years old in dog years"

print(dog_years("Lola", 16))
print(dog_years("Baby", 0), str("\n"))

#  MATH
print("Challenge 8.5")

def lots_of_math(a,b,c,d):
    first = a+b
    print(first)
    second = c-d
    print(second)
    third = first * second
    print(third)
    return third % a

print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))