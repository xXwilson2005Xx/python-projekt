import random as rand
from Mob import*
from playerstats import*

def Mob_choice(mob: mobstats):
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("\n Attack! \n")
        print("<------------------------------------------------------------->")
    elif mobchoice == 2:
        print("\n Defend! \n")
        print("<------------------------------------------------------------->")
        mob.armorclass = mob.armorclass + 1
    return mobchoice


def mobaction(player: playerstats, mob: mobstats, mobchoice):
    if mobchoice == 1:
        print("")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= player.armorclass:
            player.hp = player.hp - mob.strength
            if player.hp < 0:
                player.hp = 0
            print(f' Monster Attack succeded! Your health is redused to:' ,(player.hp),'health \n')
        else:
            print(" Monster Attack faild! \n")
    elif mobchoice == 2:
        print("")
    return mobchoice


def player_choice(player: playerstats):
    playerchoice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
    if playerchoice == 1:
        print("<------------------------------------------------------------->")
        print("\n You chossed to Attack! \n")
    elif playerchoice == 2:
        print("<------------------------------------------------------------->")
        print("\n You chossed to Defend! \n")
        player.armorclass = player.armorclass + 1

def player_combat_mob(player: playerstats, mob: mobstats, playerchoice):
    if playerchoice == 1:
        print("")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= mob.armorclass:
            mob.hp = mob.hp - player.strength
            if mob.hp < 0:
                mob.hp = 0
            print(f' Your attack succeded, now The Monster has',(mob.hp),'health \n') 
            print("<------------------------------------------------------------->")
        else:
            print(" Your Attack faild! \n")
            print("<------------------------------------------------------------->")
    else:
        print("<------------------------------------------------------------->")
    return playerchoice
    

def player_combat_boss(player: playerstats, boss: Boss_stats, playerchoice):
    if playerchoice == 1:
        print("")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= boss.armorclass:
            boss.hp = boss.hp - player.strength
            if boss.hp < 0:
                boss.hp = 0
            print(f' Your attack succeded, now The Boss has',(boss.hp),'health \n') 
            print("<------------------------------------------------------------->")
        else:
            print(" Your Attack faild! \n")
            print("<------------------------------------------------------------->")
    else:
        print("<------------------------------------------------------------->")
    return playerchoice

def boss_choice(boss: Boss_stats):
    import random as rand
    bosschoice = rand.randint(1, 2)
    if bosschoice == 1:
        print("\n The Boss chossed to Attack! \n")
        print("<------------------------------------------------------------->")
    elif bosschoice == 2:
        print("\n The Boss chossed to Defend! \n")
        print("<------------------------------------------------------------->")
        boss.armorclass = boss.armorclass + 1
    return bosschoice


def bossaction(player: playerstats, boss: Boss_stats, bosschoice):
    if bosschoice == 1:
        print(" Boss Attack!")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget >= player.armorclass:
            player.hp = player.hp - boss.strength
            if player.hp < 0:
                player.hp = 0
            print(f' Boss Attack succeded! Your health is redused to:' ,(player.hp),'health \n')
        else:
            print(" Attack faild! \n")
    elif bosschoice == 2:
        print("")
    return bosschoice
        
