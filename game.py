x = int(input("Start game! 1.YES or 2.NO: "))
if x == 1:
    print("Adventure Boys: The game!")
else:
    print("Try again later!")



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
