from playerstats import*
from Choose_player import*

def trap(player: playerstats):
    import random as rand
    trapdamage = rand.randint(1,5)
    player.hp = player.hp - trapdamage
    print('you stept in a trap and took',(trapdamage),"damage")
