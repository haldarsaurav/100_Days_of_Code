#Random Name Generator 

print("Random Name Generator.")

# Ask any random stuff from the user and checking whether they have or not 

while True:
    print("What is your best friends name?")
    friends_name = input("> ")
    if friends_name == "":
        print("You have not entered anything, please write your friends name agian.")
    else:
        break
    
while True:
    print("What is your pet's name?")
    pets_name = input("> ") 
    if pets_name == "":
        print("You have not entered anything, please enter your pets name again.")
    else:
        break
    
#print the generated name after capitalizing the entered names

x =  (f"{friends_name}" f" {pets_name}")
x = x.replace(" ", "_")
print(f"Your name can be = {x} ")