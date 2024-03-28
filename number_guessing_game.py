import random as rn

range_val = input("Enter the range of values separated with comma between 1 to 100: ")

beg,end = range_val.split(",")

for i in range(5):    
    user_input = int(input(f"Please guess the values between {beg} and {end}: "))
    system_val = rn.randint(int(beg),int(end))
    print(system_val)
    if system_val == user_input:
        print("You won")
        break
    elif user_input < system_val:
        print("You have entered small number, please try again.")
    elif user_input > system_val:
        print("You have entered larger number, please try again.")
    



