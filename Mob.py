
def mobaction():
    import random as rand
    mobchoise = rand.randint(1, 2)
    if mobchoise == 1:
        print("attack")
    else:
        print("defend")
    return mobchoise

mobaction()
