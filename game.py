from art import*
from Mob import*
from biom import*
from playerstats import*
from health_damage import*
from Start_game import*
from Choose_player import*
from combat import*

print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
printtitlescreen()
print("\n\n\n")

Start_game()

print("1", end=". ")
Wilson_Slowfoot.print_info()
print("2", end=". ")
Zacke_Swiftfoot.print_info()
print("3", end=". ")
Jacke_Bigfoot.print_info()
print("")

player = choose_player()

biom = biomer()

while True:
    mob = Random_mob()
    old_mob_armorclass = mob.armorclass
    old_player_armorclass = player.armorclass

    print(f"""
    <------------------------------->
    A wild {biom}-{mob.name} appeared
    <------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        mob.armorclass = old_mob_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{mob.name} chooses to...")
        mobchoice = Mob_choice(mob)
        mobaction(player, mob, mobchoice)
        player_combat_mob(player, mob, playerchoice)
        if mob.hp <= 0:
            print("""
            Monster DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break


    print("")
    print("King e du monstret är DÖD! \n")  
    mob_drop_item()
    print("--------------------------")
    openInventory(player)
    mob = Random_mob()
    print(f"""
    <------------------------------->
    A wild {biom}-{mob.name} appeared
    <------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        mob.armorclass = old_mob_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{mob.name} chooses to...")
        mobchoice = Mob_choice(mob)
        mobaction(player, mob, mobchoice)
        player_combat_mob(player, mob, playerchoice)
        if mob.hp <= 0:
            print("""
            Monster DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break


    print("")
    print("King e du monstret är DÖD! \n") 

    mob_drop_item()
    print("--------------------------")
    openInventory(player)

    mob = Random_mob()

    print(f"""
    <------------------------------->
    A wild {biom}-{mob.name} appeared
    <------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        mob.armorclass = old_mob_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{mob.name} chooses to...")
        mobchoice = Mob_choice(mob)
        mobaction(player, mob, mobchoice)
        player_combat_mob(player, mob, playerchoice)
        if mob.hp <= 0:
            print("""
            Monster DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break
        

    print("")
    print("King e du monstret är DÖD! \n") 

    mob_drop_item()
    print("--------------------------")
    openInventory(player)

    mob = Random_mob()

    print(f"""
    <------------------------------->
    A wild {biom}-{mob.name} appeared
    <------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        mob.armorclass = old_mob_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{mob.name} chooses to...")
        mobchoice = Mob_choice(mob)
        mobaction(player, mob, mobchoice)
        player_combat_mob(player, mob, playerchoice)
        if mob.hp <= 0:
            print("""
            Monster DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break
        

    print("")
    print("King e du monstret är DÖD! \n") 

    mob_drop_item()
    print("--------------------------")
    openInventory(player)

    mob = Random_mob()

    print(f"""
    <------------------------------->
    A wild {biom}-{mob.name} appeared
    <------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        mob.armorclass = old_mob_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{mob.name} chooses to...")
        mobchoice = Mob_choice(mob)
        mobaction(player, mob, mobchoice)
        player_combat_mob(player, mob, playerchoice)
        if mob.hp <= 0:
            print("""
            Monster DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break
        


    print("")
    print("King e du monstret är DÖD! \n")

    mob_drop_item()
    print("--------------------------")
    openInventory(player)

    boss = Random_boss()
    old_boss_armorclass = boss.armorclass

    print(f"""
    <------------------------------------------->
    A wild {biom}-{boss.name} appeared
    <------------------------------------------->
    """)

    while True:
        player.armorclass = old_player_armorclass
        boss.armorclass = old_boss_armorclass
        playerchoice = player_choice(player)
        print(f"{biom}-{boss.name} chooses to...")
        bosschoice = boss_choice(boss)
        bossaction(player, boss, bosschoice)
        player_combat_boss(player, boss, playerchoice)
        if boss.hp <= 0:
            print("""
            Boss DÖD!
            """)
            break
        if player.hp <= 0:
            print("""
            Du är död
            """)
            break
        


    print("")
    print("King e du monstret är DÖD!") 
    mob_drop_item()
    print("--------------------------")
    openInventory(player)

    if player.hp <= 0:
            print("""
            Du är död
            """)
            break



print("Game over!")