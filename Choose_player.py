from playerstats import*

def choose_player():
    while True:
        try:
            player = int(input("Choose a player: "))
            if player == 1:
                Wilson_Slowfoot.print_info()
                break
            elif player == 2:
                Zacke_Swiftfoot.print_info()
                break
            elif player == 3:
                Jacke_Bigfoot.print_info()
                break
        except:
            print("Try again")