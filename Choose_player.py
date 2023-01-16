from playerstats import*
player_health = 0
def choose_player():
    global player_health
    while True:
        try:
            player = int(input("Choose a player: "))
            if player == 1:
                Wilson_Slowfoot.print_info()
                player_health = Wilson_Slowfoot.hp
                return Wilson_Slowfoot
            elif player == 2:
                Zacke_Swiftfoot.print_info()
                player_health = Zacke_Swiftfoot.hp
                return Zacke_Swiftfoot
            elif player == 3:
                Jacke_Bigfoot.print_info()
                player_health = Jacke_Bigfoot.hp
                return Jacke_Bigfoot
        except:
            print("Try again with a number\n")
