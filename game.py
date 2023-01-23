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


current_mob = Random_mob()
print(f"A wild {biom}-{current_mob.name} appeared")

player_combat(player, current_mob)

print(f"{biom}-{current_mob.name} chooses to...")
mobaction(player, mob)



