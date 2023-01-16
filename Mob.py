from playerstats import*


def mobaction(player):
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("Attack")
        import random as rand
        hittarget = rand.randint(1, 20)
        if hittarget <= player.armorclass:
            print("Attack succeded!")
        else:
            print("Attack faild!")
    else:
        print("Defend")
    return mobchoice


mobaction()
