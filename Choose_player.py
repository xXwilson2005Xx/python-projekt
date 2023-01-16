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
                break
            elif player == 2:
                Zacke_Swiftfoot.print_info()
                player_health = Zacke_Swiftfoot.hp
                break
            elif player == 3:
                Jacke_Bigfoot.print_info()
                player_health = Jacke_Bigfoot.hp
                break
        except:
            print("Try again")
