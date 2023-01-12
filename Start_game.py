def Start_game():
    try:
        Start_the_game = int(input("Start game! 1.YES or 2.NO: "))
        if Start_the_game == 1:
                print("""
        <-------------------->
        Martin Boys: The game!
        <-------------------->
        """)
        elif Start_the_game == 2:
                print("Closing...")
                exit()
    except ValueError:
        print("try a number")
        Start_game()
        


    


