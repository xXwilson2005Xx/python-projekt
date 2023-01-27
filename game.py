from art import*
from Mob import*
from biom import*
from playerstats import*
from trap_chest import*
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

while True:
    biom = biomer()
    mob = Random_mob()

    old_player_armorclass = player.armorclass
    old_mob_armorclass = mob.armorclass

    chest_rum()

    trap(player)
    old_mob_health = mob.hp
    for mobstats in MOBS:
        mob.hp = old_mob_health
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
                <--------------------->
                    Du är död
                    GAME OVER!
                <--------------------->
                The Game is made by
                PK, Wilson and Zacke!
                <--------------------->
                """)
                quit()
        mob_drop_item()
        print("--------------------------")
        openInventory(player)

    boss = Random_boss()
    old_boss_armorclass = boss.armorclass

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
            <--------->
            Du är död
            GAME OVER!
            <--------->
            """)
            quit()

    mob_drop_item()
    print("--------------------------")
    openInventory(player)
    print("")
    print("You defeated the evil of this world, now you continue on your adventure to save Lord Martin")
    print("")