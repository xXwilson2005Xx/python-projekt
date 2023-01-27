def Start_game():
    try:
        Start_the_game = int(input("Start game! 1.YES or 2.NO: "))
        if Start_the_game == 1:
            print("""
            <--------------------------------------------------------------------------------->
             The world has been ridden in darkness and only one can save it. 
             You, the noble hero, have to save the Lord, Martin. 
             You are one of his devoted knights and have been bagged by the world to save them. 
             You must bring out light in each region of darkness.
            <--------------------------------------------------------------------------------->
            """)
            print("""
            <-------------------->
            Martin Boys: The game!
            <-------------------->
            """)  

        elif Start_the_game != 1:
            
            print("""
        Too bad, you are playing this anyway!

        <--------------------------------------------------------------------------------->
         The world has been ridden in darkness and only one can save it. 
         You, the noble hero, have to save the Lord, Martin. 
         You are one of his devoted knights and have been bagged by the world to save them. 
         You must bring out light in each region of darkness.
        <--------------------------------------------------------------------------------->
  
        <-------------------->
        Martin Boys: The game!
        <-------------------->
        """)
    except ValueError:
        print("Try a number please")
        Start_game()
