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
old_player_armorclass = player.armorclass

biom = biomer()

mob = Random_mob()
old_mob_armorclass = mob.armorclass

print(f"A wild {biom}-{mob.name} appeared")

while True:
    player.armorclass = old_player_armorclass
    mob.armorclass = old_mob_armorclass
    playerchoice = player_choice(player)
    print(f"{biom}-{mob.name} chooses to...")
    mobchoice = Mob_choice(mob)
    mobaction(player, mob, mobchoice)
    player_combat(player, mob, playerchoice)
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
print("King e du monstret är DÖD!")    