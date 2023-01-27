from playerstats import*
from Choose_player import*

def trap(player: playerstats):
    import random as rand
    trapdamage = rand.randint(1,5)
    player.hp = player.hp - trapdamage
    if trapdamage <= 2:
        print("""
<---------------------------------------------------------->
 you fell in to a pit and took""" ,(trapdamage) , """damage
<---------------------------------------------------------->
        """)
    elif 5 > trapdamage > 2:
        print("""
<----------------------------------------------------------->
 you fell in to quicksand and took""",(trapdamage),"""damage
<----------------------------------------------------------->
        """)
    elif trapdamage == 5:
         print("""
<---------------------------------------------------------------->
 you took a arrow to the chest and took""",(trapdamage),"""damage
<---------------------------------------------------------------->
         """)

def chest_rum():
    import random as rand
    chest_roomtyp = rand.randint(1,3)
    if chest_roomtyp == 1:
        print("""
<----------------------------------------------------------------->
 You find yourself in a dark room with a wooden chest in the coner
                    The chest is empty...
<----------------------------------------------------------------->
        """)
    

    elif chest_roomtyp == 2:
        print("""
<------------------------------------------------------------------------------------>
 You enter a dark cave with a foul odor after a bit of walking you find a stone chest
         You open the chest and find a old red sticky heathpotion
<------------------------------------------------------------------------------------>        
        """)
        
        for item in Inventory:
            print("Inventory\n", item.item_name)
        print("1 to take potion: 2 to leave potion")
        take_Item = int(input("-> "))
        if take_Item == 1:
            Inventory.append(healthPotion)
    
        for item in Inventory:
            print(item.item_name)
        print("<------------------------------------------------------------------------------------>")


    elif chest_roomtyp == 3:
        print("""
<------------------------------------------------------------------------------------------------------>
 a blinding light shines when you enter the room, on a marble altar is a wooden chest with golden edges
                    You open the chest and find not one but two potions
<------------------------------------------------------------------------------------------------------>
        """)
        
        for item in Inventory:
            print("Inventory\n", item.item_name)
        print("1 to take the two potions: 2 to leave potions")
        take_Item = int(input("-> "))
        if take_Item == 1:
            (Inventory.append(healthPotion))
            (Inventory.append(healthPotion))
            for item in Inventory:
                print(item.item_name)
            print("<------------------------------------------------------------------------------------------------------>")
        
