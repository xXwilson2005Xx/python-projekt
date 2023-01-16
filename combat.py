import random as rand

def player_combat():
    player_choice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
    if player_choice == 1:
        print("Attack")
    else:
        print("Defend")
    return player_choice

def player_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

player_combat()
player_hitchance()
        
