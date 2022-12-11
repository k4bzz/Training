gamers = []

def add_gamer(gamer: dict, gamers_list: list) -> list:
    if gamer["name"] and gamer["availability"]:
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")
    return gamers

add_gamer({"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequecy_table() -> dict:
    days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
    return days

count_availability = build_daily_frequecy_table()

def calculate_availability(gamers_list: list, available_frequency: dict) -> dict:
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1
    return available_frequency

calculate_availability(gamers, count_availability)
print(f"Initial availability:\n{count_availability}\n")

def find_best_night(availability_table: dict) -> str:
    best_day = ''  # CA goes without that line, but it generates warning...
    count = 0
    for key, value in availability_table.items():
        if value > count:
            best_day = key
            count = value
    return best_day

game_night = find_best_night(count_availability)
print(f"First best night: {game_night}\n")

def available_on_night(gamers_list: list, day: str) -> list:
    attending_list = [gamer for gamer in gamers_list if day in gamer["availability"]]  # CA solution!!!!
    # My original ugly code below
    # for gamer in gamers:
    #     if day in gamer["availability"]:
    #         attending_list.append(gamer["name"])
    return attending_list

attending_game_night = available_on_night(gamers, game_night)
print(f"Attending first night:\n{attending_game_night}\n")

# CA SOLUTION - not quite sure about it
# compose_email = """
# Dear {name} blyat,
#
# The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {game_night} and have a blast!
#
# Magically Yours,
# the Sorcery Society
# """
#
#
# def send_email(gamers_who_can_attend, day, game):
#     for gamer in gamers_who_can_attend:
#         print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
#
#
# send_email(attending_game_night, game_night, "Abruptly Goblins!")

def send_email(gamers_who_can_attend: list, day: str, game = "Abruptly Goblins!") -> list:
    emails_to_send = []
    for gamer in gamers_who_can_attend:
        emails_to_send.append(f"Hi {gamer['name']} blyat! Come over on {day} to play {game} blyat!")
    return emails_to_send

form_email = send_email(attending_game_night, game_night)
print(f"Emails for {game_night}:\n{form_email}\n")

# CA solution - comprehend the list of gamers that dont have GAME_NIGHT and then run the rest
# unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]

count_2nd_availability = count_availability.copy()
count_2nd_availability.pop(game_night)
print(f"Second night availability:\n{count_2nd_availability}\n")

game_night2 = find_best_night(count_2nd_availability)
print(f"Second best night:\n{game_night2}\n")

attending_game_night2 = available_on_night(gamers, game_night2)
print(f"Attending second night:\n{attending_game_night2}\n")

form_email2 = send_email(attending_game_night2, game_night2)
print(f"Emails for {game_night2}:\n{form_email2}\n")