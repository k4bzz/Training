# STRINGS
# STRINGS ARE LISTS
favorite_fruit = "blueberry"
print(favorite_fruit[0])

# SLICING
print(favorite_fruit[1:3])

# CONCATENATION
fruit_prefix = "blue"
fruit_suffix = "berries"

favorite_fruit = fruit_prefix + fruit_suffix

print(favorite_fruit)  # no spaces

fruit_sentence = "My favorite fruit is " + favorite_fruit

print(fruit_sentence)  # with spaces

# LEN
favorite_fruit = "blueberry"
length = len(favorite_fruit)
print(length)

last_char = favorite_fruit[len(favorite_fruit) - 1]
print(last_char)

length = len(favorite_fruit)
last_chars = favorite_fruit[length-4:]
print(last_chars)

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
    return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

# NEGATIVE INDICIES

favorite_fruit = 'blueberry'
print(favorite_fruit[-1])

# STRINGS ARE IMMUTABLE = CANNOT BE CHANGED
first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"      # THIS WILL PRODUCE ERROR
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)

# ESCAPE CHARACTERS
# favorite_fruit_conversation = "He said, "blueberries are my favorite!""  # DOESNT WORK
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""

# ITERATE THROUGH STRINGS
def print_each_letter(word):
    for letter in word:
        print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)

# CONDITIONS
favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
    if character == "b":
        counter = counter + 1
print(counter)

def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
    return False

# CONDITIONS PART 2
print("e" in "blueberry")  # IN checks if one string is part of another string.

# IF LETTER IN BOTH STRINGS
def contains(big_string, little_string):
    # CA SOLUTION
    return little_string in big_string

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

print(common_letters("banana", "cream"))

# SHIFT BY ONE CHARACTER WITH SLICING
def password_generator(username):
    temp_pass = username[-1] + username[:-1]
    return temp_pass

print(password_generator("AbeSimp"))

# SHIFT BY ONE CHARACTER WITH FOR
def password_generator2(username):
    password = ""
    for i in range(0, len(username)):
        password += username[i-1]
    return password

print(password_generator2("AbeSimp"))

# STRING METHODS - LOWER CASE
favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)
print(favorite_song.lower())  # lower case smooth
print(favorite_song)  # original string doesn't change = SmOoTH

# UPPER & TITLE/SENTENCE CASE
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

# SPLIT
man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())  # .split() default to splitting at spaces

greatest_guitarist = "santana"
print(greatest_guitarist.split('n'))  # => ['sa', 'ta', 'a']
print(greatest_guitarist.split('a'))  # when you split on a character the string ends you will get empty item in the end


authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

#F STRINGS - formatted strings
first_name = "ada"
age = 2
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()} second variable {first_name} and new type {age}!"
print(message)
print(type(message))
print(type(age))

fav_num = 8
num_value = 123.123123
print(f"My favourite number is {fav_num}")
print(f"My favourite number is {fav_num=}") # prints My favourite number is fav_num = 8
print(f"Formatting float to 2 decimal places {num_value:.2f}")

# PRINT WITH INTENDATIONS OR WHITESPACES
print("\tLAX")
print("\nLAX\nPIDR\nPISOS")

#STRIPPING WHITESPACES
string = " \tnoob f  \n"
r_str = string.rstrip() #RIGHT STRIP
l_str = string.lstrip() #LEFT STRIP
both_sides = string.strip() #STRIP FROM BOTH SIDES
print(both_sides)
print(l_str)
print(r_str)
print(string)

#QUOTES
print("Punk's") #double quotes good
# print('Punk's') single quotes dont work with apostrophies

#prints execution time
import time
start_time = time.time()
# main()          #code here
print("--- %s seconds ---" % (time.time() - start_time))


# JOIN
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words) # delimiter in quotes could be anyting

print(reapers_line_one)

#multi line strings
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
print(leaves_of_grass)

#Join by separators
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

#the above also has escape characters to deal with ' in the strings

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
 
print(smooth_fifth_verse)

# Join with \n
winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)

print(winter_trees_full)

# STRIP - removes whitespaces
featuring = "           rob thomas                 "
print(featuring.strip())

# STRIP specific characters
featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))

# STRIP & JOIN
love_maybe_lines = ['Always    ',
                    '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ',
                    '\n',
                    '   to conquer me home.    ']
love_maybe_lines_stripped = []

for word in love_maybe_lines:
    love_maybe_lines_stripped.append(word.strip())

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)

# REPLACE
with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_') # replace WHAT with WHAT
print(with_underscores)
# 'You_got_the_kind_of_loving_that_can_be_so_smooth'

# FIND
print('smooth'.find('t'))
# => '4'            # returns -1 is NOT FOUND

print("smooth".find('oo'))
# => '2'

# OLD FORMAT functionality
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

poem_title_card("I Hear America Singing", "Walt Whitman")

# OLD FORMAT 2 (doesnt depend on sequence)
def poem_description(publishing_date, author, title, original_work):
  poem_desc = """The poem {title} by {author} was originally published in {original_work} in {publishing_date}.""" \
  .format(publishing_date=publishing_date, author=author,
    title=title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)

# Project
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

# Split by commas
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

# Strip spaces
highlighted_poems_stripped = []

for word in highlighted_poems_list:
    highlighted_poems_stripped.append(word.strip())

print(highlighted_poems_stripped)

# Splits the list into sublists
highlighted_poems_details = []

for poems in highlighted_poems_stripped:
    highlighted_poems_details.append(poems.split(':'))

print(highlighted_poems_details)

# Split list into 3
for details in highlighted_poems_details:
    titles.append(details[0])
    poets.append(details[1])
    dates.append(details[2])

# Assemble complex string
for i in range(len(titles)):
    print("The poem \"{}\" was published by {} in {}.".format(titles[i], poets[i], dates[i]))

# r RAW formatting to fix escape characters
slash_null_sig = r"""
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""