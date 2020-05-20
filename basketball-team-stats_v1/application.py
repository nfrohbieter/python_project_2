from constants import PLAYERS

import random

def balance_teams():
    team1 = []
    team2 = []
    team3 = []
    for player in PLAYERS:
        random_number = random.randint(1,3)
        if random_number == 1 and len(team1) <6:
            team1.append(player)
        elif random_number == 2 and len(team2) <6:
            team2.append(player)
        elif random_number == 3 <6:
            team3.append(player)
        else:
            if len(team1) <6:
                team1.append(player)
            elif len(team2) <6:
                team2.append(player)
            elif len(team3) <6:
                team3.append(player)

    print(f"team 1 {team1}")
    print(f"team 2 {team2}")
    print(f"team 3 {team3}")

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

if __name__ == '__main__':
    balance_teams()

#display_options1()
#while True:
#    try:
#        user_input1 = int(input("Enter an option > "))
#    except:
#        print("Sorry wrong input. Remember only numbers 1 or 2.")
#    else:
#        if user_input1 == 1:
#            display_options2()
#            try:
#                user_input2 = int(input("Enter an option > "))
#            except:
#                print("Sorry wrong input. Remember only numbers 1-3.")
#            continue
#        elif user_input1 == 2:
#            break
#        else:
#            print("Sorry wrong input. Remember only numbers 1 or 2.")
