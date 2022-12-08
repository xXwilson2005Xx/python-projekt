class playerstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

Zacke_Swiftfoot = playerstats("Zacke Swiftfoot", 50, 18, 10)
Jacke_Bigfoot = playerstats("Jacke Slowfoot", 70, 10, 15)
Wilson_Slowfoot = playerstats("Wilson Bigfoot", 55, 14, 12)

class mobstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

PK = mobstats("PK", )
Boston = mobstats("Boston", )
Bromis = mobstats("Bromis", )
Alvino = mobstats("Alvino", )
Taxel = mobstats("Taxel", )
Jewly = mobstats("Jewly", )
Daffe_The_Destroyer = mobstats("Daffe_The_Destroyer", )
Voiti_The_Fallen = mobstats("Voiti_The_Fallen", )
