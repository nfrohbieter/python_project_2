from constants import PLAYERS

import random

Panthers = []
Bandits = []
Warriors = []


def clean_data():
    for player in PLAYERS:
        height = player.get('height')
        slice_string = slice(2)
        height = int(height[slice_string])
        player['height'] = height
        if player.get('experience') == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return PLAYERS


def balance_teams():
    for player in PLAYERS:
        random_number = random.randint(1, 3)
        if random_number == 1 and len(Panthers) < 6:
            Panthers.append(player)
        elif random_number == 2 and len(Bandits) < 6:
            Bandits.append(player)
        elif random_number == 3 and len(Warriors) < 6:
            Warriors.append(player)
        else:
            if len(Panthers) < 6:
                Panthers.append(player)
            elif len(Bandits) < 6:
                Bandits.append(player)
            elif len(Warriors) < 6:
                Warriors.append(player)
    return Panthers, Bandits, Warriors


def display_options():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("\n--- MENU ---\n")
    print("Here are your choices:")
    print("1) Display Team Stats")
    print("2) Quit\n")


def display_team_options():
    print("1) Panthers")
    print("2) Bandits")
    print("3) Warriors\n")


def display_team(team_number):
    if team_number == 1:
        print("Panthers Roster")
        print(Panthers)
    elif team_number == 2:
        print("Bandits Roster")
        print(Bandits)
    elif team_number == 3:
        print("Warriors Roster")
        print(Warriors)
    else:
        print("Invalid input. Please pick a number 1-3.")


if __name__ == '__main__':
    clean_data()
    balance_teams()
    display_team_options()
    team_input = int(input("Enter an option > "))
    display_team(team_input)

# display_options1()
# while True:
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
