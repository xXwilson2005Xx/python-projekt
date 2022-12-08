print("1.Mountain,N \n2.Desert,S \n3.Jungle,E \n4.Plains,W")

choosebiom=int(input("\nchoose a diration(nr)"))
if choosebiom == 1:
    biom = "mountain"
elif choosebiom == 2:
    biom = "Desert"
elif choosebiom == 3:
    biom = "Jungle"
elif choosebiom == 4:
    biom = "Plains"  
print(f"You whent thordes the{biom}") 
