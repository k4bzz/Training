# FILES

"""
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-files/cheatsheet
"""

"""
The with keyword invokes something called a context manager for the file that we’re calling open() on. 
This context manager takes care of opening the file when we call open() and then closing 
the file after we leave the indented block.
"""

# OPEN FILE WITH CONTEXT MANAGER
# Read file
with open("test_file.txt") as cool_doc:  # R argument is default - read
    cool_contents = cool_doc.read()
print(cool_contents)

"""
Encoding
Default - ASCII
To use - UTF, unicode_escape, windows-1252
"""

# Read ALL lines
with open("keats_sonnet.txt", encoding="unicode_escape") as keats_sonnet:  # Enc default ANSII. Unicode_escape better
    for line in keats_sonnet.readlines():
        print(line.rstrip("\n"))  # ReadLines adds extra /n .rstrip("\n") solves it

# Read SPECIFIC line
with open("keats_sonnet.txt", encoding="unicode_escape") as keats_sonnet:
    first_line = keats_sonnet.readline()  # Apparently first read saves input and then continues???
    second_line = keats_sonnet.readline()
    print(second_line)

# Writing into a file
with open("new.txt", "w") as file1:  # W is for writing
    file1.write("121212Sasaj J11OPU 2! ¬!\"£$%^&*()_+")  # REWRITES THE ENTIRE FILE IF EXISTS OR CREATES A NEW ONE!

# Append to a file
# TODO research why it is not appending on a new line
with open("new.txt", "a") as file1:  # A - append mode
    file1.write("2APPENDED TEXT2")  # Appends to end of file with no spacing?? In CA it starts from a new line...

# Read CSV file as dicionary
import csv

list_of_email_addresses = []
with open('test.csv', newline='') as users_csv:
    """
    We pass the additional keyword argument newline='' to the file opening open() function 
    so that we don’t accidentally mistake a line break in one of our data fields as a new 
    row in our CSV (https://docs.python.org/3/library/csv.html#id3).
    """
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])
    print(list_of_email_addresses)

# Different delimiters
import csv

# TODO newline='' doesnt read file correctly if it hase \n or just new line -> see test2.csv
with open('test2.csv', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row['Address'])