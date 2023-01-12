class playerstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in, level_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in
        self.level = level_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass} Level: {self.level}")

Zacke_Swiftfoot = playerstats("Zacke Swiftfoot", 50, 18, 10, 1)
Jacke_Bigfoot = playerstats("Jacke Bigfoot", 70, 12, 15, 1)
Wilson_Slowfoot = playerstats("Wilson Slowfoot", 55, 15, 12, 1)

class mobstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in, level_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in
        self.level = level_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass} Level: {self.level}")

PK = mobstats("PK", 60, 10, 8, 1)
Boston = mobstats("Boston", 60, 10, 8, 1)
Bromis = mobstats("Bromis", 60, 10, 8, 1)
Alvino = mobstats("Alvino", 60, 10, 8, 1)
Taxel = mobstats("Taxel", 60, 10, 8, 1)
Jewly = mobstats("Jewly", 60, 10, 8, 1)
Daffe_The_Destroyer = mobstats("Daffe The Destroyer", 65, 12, 10, 1)
Voiti_The_Fallen = mobstats("Voiti The Fallen", 65, 12, 10, 1)