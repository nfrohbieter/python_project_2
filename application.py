#import constants

import random

def display_options1():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("\n--- MENU ---\n")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit\n")

def display_options2():
    print("1) Panthers")
    print("2) Bandits")
    print("3) Warriors\n")

display_options1()
while True:
    try:
        user_input1 = int(input("Enter an option > "))
    except:
        print("Sorry wrong input. Remember only numbers 1 or 2.")
    else:
        if user_input1 == 1:
            # do later
            continue
        elif user_input1 == 2:
            break
        else:
            print("Sorry wrong input. Remember only numbers 1 or 2.")
