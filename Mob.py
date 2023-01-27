
from playerstats import*
import random as rand
from Choose_player import*

class mobstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in

    def __str__(self) -> str:
        return self.name + " Strength: " + str(self.strength)

    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

class Boss_stats():
    def __init__(self, name_in, hp_in, strength_in, armorclass_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in
    
    def print_info(self):
        print(f"Name: {self.name} Healthpool: {self.hp} Strength: {self.strength} Armorclass: {self.armorclass}")

PK = mobstats("PK", 55, 10, 9)
Boston = mobstats("Boston", 20, 20, 5)
Bromis = mobstats("Bromis", 45, 9, 9)
Alvino = mobstats("Alvino", 55, 10, 9)
Taxel = mobstats("Taxel", 40, 12, 8)
Jewly = mobstats("Jewly", 60, 9, 10)
Daffe_The_Destroyer = Boss_stats("Daffe The Destroyer", 65, 14, 12)
Voiti_The_Fallen = Boss_stats("Voiti The Fallen", 75, 10, 14)

MOBS = [PK,
Boston,
Bromis,
Alvino,
Taxel,
Jewly]

BOSS = [Daffe_The_Destroyer,
Voiti_The_Fallen,]

def Random_mob():
    import random as rand
    mob_spawn = rand.choice(MOBS)
    return mob_spawn

Random_mob()

def Random_boss():
    import random as rand
    boss_spawn = rand.choice(BOSS)
    return boss_spawn

def mob_drop_item():
    for item in Inventory:
        print(item.item_name)
    print("1 to take potion: 2 to leave potion")
    take_Item = int(input("-> "))
    if take_Item == 1:
        Inventory.append(healthPotion)
    
        for item in Inventory:
            print(item.item_name)

    elif take_Item == 2:
        pass