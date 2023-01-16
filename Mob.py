
def mobaction():
    import random as rand
    mobchoice = rand.randint(1, 2)
    if mobchoice == 1:
        print("attack")
    else:
        print("defend")
    return mobchoice



def mob_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

    
mob_hitchance()