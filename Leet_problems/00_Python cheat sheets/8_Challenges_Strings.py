# Function that counts unique letters
def unique_english_letters(word: str) -> int:
    checked_letters = []
    count = 0

    for letter in word:
        if letter not in checked_letters:
            count += 1
            checked_letters.append(letter)
    return count

print(unique_english_letters("applewr"))

""" 
CA Solution

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters2(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques
"""

# Count occurrences - single char
def count_char_x(word: str, letter: str) -> int:
    return word.count(letter)

print(count_char_x("mississippi", "s"))

"""
CA Solution

def count_char_x(word, x):
  occurrences = 0
  for letter in word:
    if letter == x:
      occurrences += 1
  return occurrences
"""

# Count occurrences - sub string
# Below cheating :P
# def count_char_x(word: str, letter: str) -> int:
#     return word.count(letter)
#
# print(count_char_x("mississippi", "iss"))

def count_multi_char_x(word: str, substring: str) -> int:
    position = 0
    count = 0
    while position < len(word) - len(substring):
        if word[position:position+len(substring)] == substring:
            count += 1
        position += 1
    return count

print(count_multi_char_x("mississippi", "iss"))

#CA Solution
def count_multi_char_x2(word, x):
  splits = word.split(x)  # splits the sting into intervals ['m', '', 'ippi', 'nax', '']
  print(splits)
  return len(splits)-1  # there will be always one more interval

print(count_multi_char_x2("mississwissbissc", "iss"))

# Substring between start and end
def substring_between_letters(word: str, start: str, end: str) -> str:
    if word.find(start) == -1 or word.find(end) == -1:
        return word
    else:
        substring = word[word.find(start)+1: word.find(end)]
    return substring

print(substring_between_letters("apple", "p", "e"))

# If length of a word is greater than smth
def x_length_words(sentence: str, length: int) -> bool:
    for word in sentence.split(" "):
        if len(word) < length:
            return False
    return True

print(x_length_words("i like apples", 2))