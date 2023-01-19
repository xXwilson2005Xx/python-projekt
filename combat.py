import random as rand
from playerstats import*

def player_combat():
    try:
        player_choice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
        if player_choice == 1:
            print("Attack")
        else:
            print("Defend")
        return player_choice
    except ValueError:
        print("Try a number please")
        player_combat()

def player_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

def Random_mob():

    import random as rand
    mob_spawn = rand.choice(MOBS)
    return mob_spawn

Random_mob()

        
