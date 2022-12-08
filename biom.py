print("1.Winter,S \n2.Desert,S \n3.Jungle,E \n4.Plains,W")

biom=int(input("\nvälj en riktning:(nr)"))
if biom == 1:
    biom = "Winter"
elif biom == 2:
    biom = "Desert"
elif biom == 3:
    biom = "Jungle"
elif biom == 4:
    biom = "Plains"  
print(f"you whent to {biom}") 
