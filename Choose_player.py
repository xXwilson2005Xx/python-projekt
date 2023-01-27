from playerstats import*
# den här klassen är för vår healing posion, den ger ut namnet och även hur mycket den ska heala
class Item:
    def __init__(self, item_name, healing_power):
        self.item_name = item_name
        self.healing_power = healing_power

healthPotion = Item("Health Potion", 30)

Inventory = [healthPotion]

player_health = 0
# denna funktion gör så att du kan välja vilken karaktär su vill spela med och berättar även en backstory om karaktären
def choose_player():
    global player_health
    while True:
        try:
            player = int(input("Choose a player: "))
            if player == 1:
                print("")
                Wilson_Slowfoot.print_info()
                print("""
<----------------------------------------------------------------------------->
 This knight, a modest knight of calm temper and reasonable strength. 
 He has trained all his life to serve under Lord Martin. 
 He would rather die standing in the light than live kneeling in the darkness.
<----------------------------------------------------------------------------->
                """)
                player_health = Wilson_Slowfoot.hp
                return Wilson_Slowfoot
            elif player == 2:
                print("")
                Zacke_Swiftfoot.print_info()
                print("""
<---------------------------------------------------------------------------------->
 A younger knight of energetic nature and usually follows his own train of thought. 
 He is highly skilled but lacks discipline. 
 He rather strike first than get stricken. But he gets the job done.
<----------------------------------------------------------------------------------> 
                """)
                player_health = Zacke_Swiftfoot.hp
                return Zacke_Swiftfoot
            elif player == 3:
                print("")
                Jacke_Bigfoot.print_info()
                print("""
<-------------------------------------------------------------------------->
 One of Lord Martin's oldest and most devoted knights. 
 He might be of older statute but he is known to be able to take a beating. 
 But he doesn't shy away from handing out beatings either.
<-------------------------------------------------------------------------->
                """)
                player_health = Jacke_Bigfoot.hp
                return Jacke_Bigfoot
        except:
            print("Try again with a number\n")

# den här funktione öppnar spelarens inventory som visar vad personen har i inventoryt och sen om den vill använda nånting från inventoryt
def openInventory(player: playerstats):
    print(player.hp)
    for item in Inventory:
        print(item.item_name,"healingpower",item.healing_power)

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
            print(item.item_name,"healingpower",item.healing_power)
        print(player.hp)
        
    elif inventory_choice == 2:
        pass
    

        
