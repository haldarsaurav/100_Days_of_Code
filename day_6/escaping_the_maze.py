# Escaping the Maze

#  _________                                         ___ ___          .__       .___                
# /   _____/_____    __ __ _______ _____   ___  __  /   |   \ _____   |  |    __| _/_____   _______ 
# \_____  \ \__  \  |  |  \\_  __ \\__  \  \  \/ / /    ~    \\__  \  |  |   / __ | \__  \  \_  __ \
# /        \ / __ \_|  |  / |  | \/ / __ \_ \   /  \    Y    / / __ \_|  |__/ /_/ |  / __ \_ |  | \/
#/_______  /(____  /|____/  |__|   (____  /  \_/    \___|_  / (____  /|____/\____ | (____  / |__|   
#       \/      \/                     \/                \/       \/            \/      \/         

# Start Of Program---------------------------------------------------------------------------------------------------------

#  https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()