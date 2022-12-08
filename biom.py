print("1.Mountain,N \n2.Desert,S \n3.Jungle,E \n4.Plains,W")

choosebiom=int(input("\nchoose a diration(nr): "))
if choosebiom == 1:
    biom = "mountain"
elif choosebiom == 2:
    biom = "Desert"
elif choosebiom == 3:
    biom = "Jungle"
elif choosebiom == 4:
    biom = "Plains"  
else:
    print("Your stupid shithead write 1, 2, 3 or 4!")

print(f"You whent towards the {biom}") 
