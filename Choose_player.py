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
                print("")
                Wilson_Slowfoot.print_info()
                player_health = Wilson_Slowfoot.hp
                return Wilson_Slowfoot
            elif player == 2:
                print("")
                Zacke_Swiftfoot.print_info()
                player_health = Zacke_Swiftfoot.hp
                return Zacke_Swiftfoot
            elif player == 3:
                print("")
                Jacke_Bigfoot.print_info()
                player_health = Jacke_Bigfoot.hp
                return Jacke_Bigfoot
        except:
            print("Try again with a number\n")

healthPotion = Item("Health Potion", 55)

Inventory = [healthPotion]



def openInventory(player: playerstats):
    print(player.hp)
    for item in Inventory:
        print(item.item_name)

    print("1: use item, 2: exit inventory")

    inventory_choice = int(input("-> "))

    if inventory_choice == 1:
        print("Choose item to use, starting with 1..")

        item_to_take = int(input("-> "))
        item_to_take -= 1

        item_to_use = Inventory[item_to_take]

        player.hp += item_to_use.healing_power

        if player.hp > player.maxhp:
            player.hp = player.maxhp

        Inventory.pop(item_to_take)

        for item in Inventory:
            print(item.item_name)
        print(player.hp)
        
    elif inventory_choice == 2:
        pass
    

        
