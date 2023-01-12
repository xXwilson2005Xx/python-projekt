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

choose_player()
biom = biomer()

print(f"A wild {biom}-{PK.name} appeared") 


