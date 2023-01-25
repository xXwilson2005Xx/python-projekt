
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
        return self.name + " Strength: " + str(self.strength)

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

def Mob_choice(mob: mobstats):
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("")
    elif mobchoice == 2:
        print("Defend")
        mob.armorclass = mob.armorclass + 1
    return mobchoice


def mobaction(player: playerstats, mob: mobstats, mobchoice):
    if mobchoice == 1:
        print("Attack")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= player.armorclass:
            player.hp = player.hp - mob.strength
            print("Attack succeded!")
            print(f'Your health is redused to:' ,(player.hp),)
        else:
            print("Attack faild!")
    elif mobchoice == 2:
        print("")
    return mobchoice


def player_choice(player: playerstats):
    playerchoice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
    if playerchoice == 1:
        print("")
    elif playerchoice == 2:
        print("Defend!")
        player.armorclass = player.armorclass + 1
    return playerchoice

def player_combat(player: playerstats, mob: mobstats, playerchoice):
    try:
        if playerchoice == 1:
            print("Attack")
            import random as rand
            hittarget = rand.randint(1, 20)
            if hittarget >= mob.armorclass:
                mob.hp = mob.hp - player.strength
                print(f'Your attack succeded, now the monster has',(mob.hp),'health')
            else:
                print("Attack faild!")
        else:
            print("Defend")
        return playerchoice
    except ValueError:
        print("Try a number please")
        player_combat()
