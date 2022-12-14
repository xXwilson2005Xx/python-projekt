
def mobaction():
    import random as rand
    mobchoise = rand.randint(1, 2)
    if mobchoise == 1:
        print("attck")
    else:
        print("defend")
    return mobchoise

mobaction()
