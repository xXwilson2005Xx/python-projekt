print(" Adventure Boys: The game")

class playerstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

Zacke_Swiftfoot = stats("Zacke Swiftfoot", 50, 18, 10)
Jacke_Bigfoot = stats("Jacke Slowfoot", 70, 10, 15)
Wilson_Slowfoot = stats("Wilson Bigfoot", 55, 14, 12)
