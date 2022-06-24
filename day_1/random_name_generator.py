#Random Name Generator 

#  _________                                         ___ ___          .__       .___                
# /   _____/_____    __ __ _______ _____   ___  __  /   |   \ _____   |  |    __| _/_____   _______ 
# \_____  \ \__  \  |  |  \\_  __ \\__  \  \  \/ / /    ~    \\__  \  |  |   / __ | \__  \  \_  __ \
# /        \ / __ \_|  |  / |  | \/ / __ \_ \   /  \    Y    / / __ \_|  |__/ /_/ |  / __ \_ |  | \/
#/_______  /(____  /|____/  |__|   (____  /  \_/    \___|_  / (____  /|____/\____ | (____  / |__|   
#       \/      \/                     \/                \/       \/            \/      \/         

# Start Of Program---------------------------------------------------------------------------------------------------------

print("Random Name Generator.")

# Ask any random stuff from the user and checking whether they have or not 

while True:
    print("What is your best friends name?")
    friends_name = input("> ")
    if friends_name == "":
        print("You have not entered anything, please write your friends name agian.\n")
    else:
        break
    
while True:
    print("What is your pet's name?")
    pets_name = input("> ") 
    if pets_name == "":
        print("You have not entered anything, please enter your pets name again.\n")
    else:
        break
    
#print the generated name after capitalizing the entered names

fn = friends_name.title()
pn = pets_name.title()

print(f"Your name cane be = {fn} {pn}\n")