# coding=unicode_escape

import datetime
class Menu:
    def __init__(self, name: str, items: dict, start_time: datetime.time(), end_time: datetime.time()) -> None:
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return f"Menu {self.name} available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items: dict) -> float:
        bill = 0
        for item in purchased_items:
            bill += self.items[item] * purchased_items[item]
        return bill


class Franchise:
    def __init__(self, name: str, address: str, menus) -> None:
        self.name = name
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return f"It is {self.name} located at {self.address}"

    # TODO figure out how not to no print stuff in method and return the list or smth
    def available_menus(self, time: datetime.time()) -> None:
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                print(f"You are at {self.name}. Current time is {time} the following menu is available {menu.name} "
                      f"as it operates from {menu.start_time} to {menu.end_time}. Items are {menu.items}")
            else:
                print(f"Menu {menu.name} is not available at {time}") # Menu {menu} will trigger __repr__!! so menu.name


class Businees:
    def __init__(self, name: str, franchises: list) -> None:
        self.name = name
        self.franchises = franchises


arepas_menu = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
}

arepas = Menu("Take a' Arepa", arepas_menu, datetime.time(10, 00), datetime.time(20, 00))

brunch_menu = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}

brunch = Menu("brunch", brunch_menu, datetime.time(11, 00), datetime.time(16, 00))

early_bird_menu = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}

early_bird = Menu("early_bird", early_bird_menu, datetime.time(15, 00), datetime.time(18, 00))

dinner_menu = {
    'crostini with eggplant caponata': 13.00,
    'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
}

dinner = Menu("dinner", dinner_menu, datetime.time(17, 00), datetime.time(23, 00))

kids_menu = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}

kids = Menu("kids", kids_menu, datetime.time(11, 00), datetime.time(21, 00))
print(kids)
print(arepas)

print(brunch.calculate_bill({"pancakes": 1, "home fries": 1, "coffee": 1}))
print(early_bird.calculate_bill({"salumeria plate": 1, "mushroom ravioli (vegan)": 1}))

menu_list = [kids, brunch, early_bird, dinner, arepas]

flagship_store = Franchise("Main store", "1232 West End Road", menu_list)
new_installment = Franchise("New store","12 East Mulberry Street", menu_list)
arepas_place = Franchise("SOOKA", "189 Fitzgerald Avenue", menu_list)
print(new_installment)

new_installment.available_menus(datetime.time(12, 00)) # Franchise.available_menus won't work as it is instance method
flagship_store.available_menus(datetime.time(17, 00))
arepas_place.available_menus(datetime.time(12, 00))

business_one = Businees("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
business_two = Businees("Take a' Arepa", [arepas_place])