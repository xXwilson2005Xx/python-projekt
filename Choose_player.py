from playerstats import*

def choose_player():
    player = int(input("Choose a player: "))
    if player == 1:
        Wilson_Slowfoot.print_info()
    elif player == 2:
        Zacke_Swiftfoot.print_info()
    elif player == 3:
        Jacke_Bigfoot.print_info()
    else:
        print("Try again")
    return player