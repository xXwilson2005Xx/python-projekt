
from playerstats import*
import random as rand
from Choose_player import*

class mobstats():

    def __init__(self, name_in, hp_in, strength_in, armorclass_in, level_in):
        self.name = name_in
        self.hp = hp_in
        self.strength = strength_in
        self.armorclass = armorclass_in
        self.level = level_in

    def __str__(self) -> str:
        return self.name + " Strength" + str(self.strength)

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

MOBS = [PK,
Boston,
Bromis,
Alvino,
Taxel,
Jewly]


def Random_mob():

    import random as rand
    mob_spawn = rand.choice(MOBS)
    return mob_spawn

Random_mob()

mob = Random_mob()


def mobaction(player: playerstats, mob: mobstats):
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("Attack")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget <= player.armorclass:
            player.hp = player.hp - mob.strength
            print("Attack succeded!")
            print(player.hp)
        else:
            print("Attack faild!")
    else:
        print("Defend")
    return mobchoice

