"""
Opening your comic book store, the Sorcery Society, has been a lifelong dream come true. You quickly diversified your
shop offerings to include miniatures, plush toys, collectible card games, and board games.
Eventually, the store became more a games store with a selection of this week's newest comic
books and a small offering of graphic novel paperbacks. Completing your transformation means offering
space for local tabletop gamers. They love to play their favorite RPG, \"Abruptly Goblins!\" and will happily pay
you per chair to secure the space to do it. Unfortunately, planning the game night has fallen to you. If you pick the
wrong night, not enough people will come and the game night will be cancelled. You decide it's best that you automate
the game night selector to get the most people through the door. First you need to create a list of people who will be
attending the game night.

Create an empty list called `gamers`. This will be your list of people who are attending game night.
"""

"""
Now we want to create a function that will update this list and add a new gamer to the this `gamers` list. Each `gamer` 
should be a dictionary with the following keys:",
- "name": a string that contains the gamer's full or presumed name. E.g., "Vicky Very",
- "availability": a list of strings containing the names of the days of the week that the gamer is available. 
E.g., ["Monday", "Thursday", "Sunday"]

Instructions
Create a function called `add_gamer` that takes two parameters: `gamer` and `gamers_list`. 
The function should check that the argument passed 
to the `gamer` parameter has both "name" and a "availability" as keys and if so add `gamer` to `gamers_list`."
"""