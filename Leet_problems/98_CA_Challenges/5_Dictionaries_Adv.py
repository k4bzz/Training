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
    unique_list = []

    for value in my_dictionary.values():
        if value not in unique_list:
            unique_list.append(value)
    return len(unique_list)


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))


# Make a dictionary of a first letter of a key and a count of values
def count_first_letter(names: dict) -> dict:
    new_dict = {}
    for surname in names.keys():
        for _ in names[surname]:
            if surname[0] in new_dict:
                new_dict[surname[0]] += 1
            else:
                new_dict[surname[0]] = 1
    return new_dict


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"],
                          "Snow": ["Jon"],
                          "Lannister": ["Jaime", "Cersei", "Tywin"]}))

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"],
                          "Snow": ["Jon"],
                          "Sannister": ["Jaime", "Cersei", "Tywin"]}))

"""
CA Solution - better
def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters
"""
