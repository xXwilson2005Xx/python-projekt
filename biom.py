print("Winter,1 \nDesert,2 \nJungle,3 \nPlains,4")

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
