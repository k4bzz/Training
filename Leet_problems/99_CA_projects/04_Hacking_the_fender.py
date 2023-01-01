import csv
import json

compromised_users = []

# Reads the CSV file and creates list of usernames
with open("passwords.csv", newline="") as password_file:
    password_csv = csv.DictReader(password_file)
    for row in password_csv:
        password_row = row
        compromised_users.append(password_row["Username"])

# Writes the list of usernames into a TXT file
with open("compromised_users.txt", "w") as compromised_users_file:
    for i, user in enumerate(compromised_users):
        # Check for last items
        if i == (len(compromised_users) - 1):
            compromised_users_file.write(user)
        else:
            compromised_users_file.write(f"{user},")

# Write dictionary into JSON
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

# ???
with open("new_password.csv", "w") as new_password_object:
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
    new_password_object.write(slash_null_sig)