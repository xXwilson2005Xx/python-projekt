from art import*
from Mob import*
from biom import*
from playerstats import*
from health_damage import*
from Start_game import*
from Choose_player import*
from player_combat import*

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

mob = Random_mob()

print(f"A wild {biom}-{mob.name} appeared")

while True:
    player_combat(player, mob)
    print(f"{biom}-{mob.name} chooses to...")
    mobaction(player, mob)
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