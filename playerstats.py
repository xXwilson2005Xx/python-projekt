
#  Den här klassen ger alla players stats alltså, namn, hp, maxhp, styrka och armorclass
class playerstats():

    def __init__(self, name_in, hp_in, maxhp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.maxhp = maxhp_in
        self.strength = strength_in
        self.armorclass = armorclass_in
    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

Zacke_Swiftfoot = playerstats("Zacke Swiftfoot", 50, 50, 18, 12)
Jacke_Bigfoot = playerstats("Jacke Bigfoot", 70, 70, 12, 16) 
Wilson_Slowfoot = playerstats("Wilson Slowfoot", 55, 55, 15, 14)