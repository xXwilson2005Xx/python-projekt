class playerstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

Zacke_Swiftfoot = playerstats("Zacke Swiftfoot", 50, 18, 10)
Jacke_Bigfoot = playerstats("Jacke Bigfoot", 70, 12, 15)
Wilson_Slowfoot = playerstats("Wilson Slowfoot", 55, 15, 12)

class mobstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

PK = mobstats("PK", 60, 10, 8)
Boston = mobstats("Boston", 60, 10, 8)
Bromis = mobstats("Bromis", 60, 10, 8)
Alvino = mobstats("Alvino", 60, 10, 8)
Taxel = mobstats("Taxel", 60, 10, 8)
Jewly = mobstats("Jewly", 60, 10, 8)
Daffe_The_Destroyer = mobstats("Daffe_The_Destroyer", 65, 12, 10)
Voiti_The_Fallen = mobstats("Voiti_The_Fallen", 65, 12, 10)