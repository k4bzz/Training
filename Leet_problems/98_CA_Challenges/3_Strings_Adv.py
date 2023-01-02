# Check if name is in string
def check_for_name(sentence: str, name: str) -> bool:
    if sentence.lower().count(name.lower()):
        return True
    return False

print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is JAMIE", "Jamie"))

"""
CA Solution

def check_for_name(sentence, name):
    return name.lower() in sentence.lower()
"""

# Print every other letter
def every_other_letter(word: str) -> str:
    return word[::2]

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

# Print reverse string
def reverse_string(word: str) -> str:
    return word[::-1]

print(reverse_string("Codecademy"))
print(reverse_string("Hello World!"))
print(reverse_string(""))

# Swap first letters
def make_spoonerism(word1: str, word2: str) -> str:
    spoonerism = word2[0] + word1[1:] + " " + word1[0] + word2[1:]
    return spoonerism

print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))

# Adds exclamation marks until makes the required length
def add_exclamation(word: str) -> str:
    if len(word) < 20:
        new_line = str(word)
        return new_line + ("!"*(20-len(word)))
    else:
        return word

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))

"""
CA Solution
def add_exclamation(word):
    while(len(word) < 20):
        word += "!"
    return word
"""