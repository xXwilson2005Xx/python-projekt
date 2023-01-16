import random as rand

def player_combat():
    import random as rand
    player_choice = rand.randint(1, 2)
    if player_choice == 1:
        print("attack")
    else:
        print("defend")
    return player_choice

def player_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

player_hitchance()
        
