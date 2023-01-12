
def mobaction():
    import random as rand
    mobchoise = rand.randint(1, 2)
    if mobchoise == 1:
        print("attack")
    else:
        print("defend")
    return mobchoise



def hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

    
hitchance()