def biomer():
    try:
        print(""""

        <------------->
         1.Mountain,N 
         2.Desert,S 
         3.Jungle,E 
         4.Plains,W
        <------------->
        """)
        choosebiom=int(input("\nChoose a diraction(number): "))
        if choosebiom == 1:
            biom = "Mountains"
        elif choosebiom == 2:
            biom = "Desert"
        elif choosebiom == 3:
            biom = "Jungle" 
        elif choosebiom == 4:
            biom = "Plains"  
        else:
            print("""
            <-------------------------------------->
            Your stupid shithead write 1, 2, 3 or 4!
            <-------------------------------------->
            """)

        print(f"""
        <-------------------------->
        You went towards the {biom}!
        <-------------------------->
        """) 
        return biom

    except ValueError:
        print("Try a number please\n")
        biomer()
