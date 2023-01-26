from playerstats import*

class Item:
    def __init__(self, item_name, healing_power):
        self.item_name = item_name
        self.healing_power = healing_power

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

healthPotion = Item("Health Potion", 10)

Inventory = [healthPotion]



def openInventory():
    for item in Inventory:
        print(item.item_name)

    print("1: use item, 2: exit inventory")

    inventory_choice = int(input("-> "))

    if inventory_choice == 1:
        print("Choose item to use, starting wit 1..")

        item_to_take = int(input("-> "))

        item_to_use = Inventory[item_to_take]

        player_health += item_to_use.healing_power
        
    elif inventory_choice == 2:
        pass
    

        
