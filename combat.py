import random as rand
from Mob import*
from playerstats import*

def Mob_choice(mob: mobstats):
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("\n Monster chossed to Attack! \n")
        print("<------------------------------------------------------------->")
    elif mobchoice == 2:
        print("\n Monster chossed to Defend! \n")
        print("<------------------------------------------------------------->")
        mob.armorclass = mob.armorclass + 1
    return mobchoice


def mobaction(player: playerstats, mob: mobstats, mobchoice):
    if mobchoice == 1:
        print(" Monster Attack!")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= player.armorclass:
            player.hp = player.hp - mob.strength
            print(f' Monster Attack succeded! Your health is redused to:' ,(player.hp),'health \n')
        else:
            print(" Attack faild! \n")
    elif mobchoice == 2:
        print("")
    return mobchoice


def player_choice(player: playerstats):
    playerchoice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
    if playerchoice == 1:
        print("<------------------------------------------------------------->")
        print("\n You chossed to Attack! \n")
    elif playerchoice == 2:
        print("\n You chossed to Defend! \n")
        player.armorclass = player.armorclass + 1
    return playerchoice

def player_combat(player: playerstats, mob: mobstats, playerchoice):
    try:
        if playerchoice == 1:
            print(" Your Attack!")
            import random as rand
            hittarget = rand.randint(1, 20)
            if hittarget >= mob.armorclass:
                mob.hp = mob.hp - player.strength
                print(f' Your attack succeded, now the monster has',(mob.hp),'health \n') 
                print("<------------------------------------------------------------->")
            else:
                print(" Attack faild! \n")
                print("<------------------------------------------------------------->")
        else:
            print("<------------------------------------------------------------->")
        return playerchoice
    except ValueError:
        print(" Try a number please \n")
        player_combat()



        
