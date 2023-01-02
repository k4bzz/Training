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