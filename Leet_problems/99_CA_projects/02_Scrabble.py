def score_word(word: str) -> int:
    word_up = word.upper()
    point_total = 0

    for letter in word_up:
        point_total += letter_to_points[letter]

    return point_total


def play_word(curr_player: str, new_word: str) -> None:
    player_to_words[curr_player].append(new_word)


def update_point_totals(curr_words: list) -> int:
    player_points = 0
    for guessed_word in curr_words:
        player_points += score_word(guessed_word)
    return player_points


# Define params
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

player_to_words = {"player1": ["Blue", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}


play_word("player1", "xxxyyyJJJJzzzzz")

player_to_points = {}

for player, words in player_to_words.items():
    # player_points = 0
    # for guessed_word in words:
    #     player_points += score_word(guessed_word)
    # update_point_totals(words)
    player_to_points[player] = update_point_totals(words)

print(player_to_points)
