import random as rand
from Mob import*
from playerstats import*

def player_combat(player: playerstats, mob: mobstats):
    try:
        player_choice = int(input("Do you want to Attack or Defend? 1:Attack 2:Defend: "))
        
        if player_choice == 1:
            print("Attack")
            import random as rand
            hittarget = rand.randint(1, 20)
            if hittarget <= mob.armorclass:
                mob.hp = mob.hp - player.strength
                print(f'Your succeded, now the monster has',(mob.hp),'health')
            else:
                print("Attack faild!")
        else:
            print("Defend")
        return player_choice
    except ValueError:
        print("Try a number please")
        player_combat()

def player_hitchance():
    import random as rand
    hittarget = rand.randint(1, 20)
    print(hittarget)
    return hittarget

        
