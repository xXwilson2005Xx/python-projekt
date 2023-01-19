import random as rand

def player_combat():
    try:
        player_choice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
        if player_choice == 1:
            print("Attack")
        else:
            print("Defend")
        return player_choice
    except ValueError:
        print("Try a number please")
        player_combat()

def player_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget


        
