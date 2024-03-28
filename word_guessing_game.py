import random

list_val = ['Apple','Banana','Mango','Cherry','Papaya','Melon']

for _ in range(3):
    
    for l in list_val:
        print(l)
    user_in = input("Please guess the fruit from above list: ")
    system_choice = random.choice(list_val)
    #print(system_choice)
    if user_in.lower() == system_choice.lower():
        print("You won")
        break
    else:
        print("You Loose")