"""
https://www.codecademy.com/learn/learn-intermediate-python-3/modules/int-python-function-arguments/cheatsheet
"""

# Positional arguments - called by order
def print_name(first_name, last_name):
    print(first_name, last_name)


print_name('Jiho', 'Baggins')

# Keyword arguments = assigned by calling by name, order doesnt matter
def print_name(first_name, last_name):
    print(first_name, last_name)


print_name(last_name='Baggins', first_name='Jiho')

# Default arguments - can be omitted, in whic case will return the default value
def print_name(first_name='Jiho', last_name='Baggins'):
    print(first_name, last_name)


print_name()

# Exercise
tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

def assign_table(table_number: int, name: str, vip_status: bool) -> dict:
    tables[table_number] = [name, vip_status]
    return tables

"""
my_dict = {}
my_dict.update({'key': 'value'})
"""


print(assign_table(2, "XYJ", True))