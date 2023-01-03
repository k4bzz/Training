# Mere words and their lengths into dictionary
def word_length_dictionary(words: list) -> dict:
    lengths = []
    for word in words:
        lengths.append(len(word))
    new_dict = dict(zip(words, lengths))
    return new_dict


print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))

"""
CA Solution

def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths
"""


# Creates a dictionary with frequency of words in the list
def frequency_dictionary(words: list) -> dict:
    freq_dict = {}
    for word in words:
        freq_dict[word] = words.count(word)
    return freq_dict


print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0, 0, 0, 0, 0]))

# Return number of unique values from dictionary
def unique_values(my_dictionary: dict) -> int:
    counter = 0
    # print(list(my_dictionary.values()))

    for value in my_dictionary.values():
        print(f" value {value} count {list(my_dictionary.values()).count(value)}")
        if list(my_dictionary.values()).count(value) == 1:
            counter += 1
    return counter


print(unique_values({0: 3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))

# print(dir(list))
