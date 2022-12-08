print("1.Mountain,N \n2.Desert,S \n3.Jungle,E \n4.Plains,W")

chosebiom=int(input("\nchose a diration(nr): "))
if chosebiom == 1:
    biom = "mountain"
elif chosebiom == 2:
    biom = "Desert"
elif chosebiom == 3:
    biom = "Jungle"
elif chosebiom == 4:
    biom = "Plains"  
print(f"You whent thordes the{biom}") 
