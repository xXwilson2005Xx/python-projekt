def decrease_player_health(damage):
    global player_health
    player_health = player_health - damage

def poison_gas():
    poison_gas = 5
    decrease_player_health(poison_gas)

def fall_pit():
    fall_pit = 3
    decrease_player_health(fall_pit)

def increase_player_health(healing):
    global player_health
    player_health = player_health + healing

def healing_posion():
    healing_posion = 30
    increase_player_health(healing_posion)