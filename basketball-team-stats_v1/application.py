from constants import PLAYERS

from constants import TEAMS

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
    max_players = len(PLAYERS) / len(TEAMS)
    yes_experience = []
    no_experience = []

    for player in PLAYERS:
        if player.get("experience") == "YES":
            yes_experience.append(player)
        else:
            no_experience.append(player)

    for player in yes_experience:
        random_number = random.randint(1, 3)
        if random_number == 1 and len(Panthers) < max_players / 2:
            Panthers.append(player)
        elif random_number == 2 and len(Bandits) < max_players / 2:
            Bandits.append(player)
        elif random_number == 3 and len(Warriors) < max_players / 2:
            Warriors.append(player)
        else:
            if len(Panthers) < max_players / 2:
                Panthers.append(player)
            elif len(Bandits) < max_players / 2:
                Bandits.append(player)
            elif len(Warriors) < max_players / 2:
                Warriors.append(player)

    for player in no_experience:
        random_number = random.randint(1, 3)
        if random_number == 1 and len(Panthers) < max_players:
            Panthers.append(player)
        elif random_number == 2 and len(Bandits) < max_players:
            Bandits.append(player)
        elif random_number == 3 and len(Warriors) < max_players:
            Warriors.append(player)
        else:
            if len(Panthers) < max_players:
                Panthers.append(player)
            elif len(Bandits) < max_players:
                Bandits.append(player)
            elif len(Warriors) < max_players:
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


def display_team_stats(team_number):
    team_output = 0
    team_name = 0
    total_players = 0
    total_height = 0
    experienced_players = 0
    inexperienced_players = 0
    average_height = 0

    if team_number == 1:
        team_output = Panthers
        team_name = "Panthers"
    elif team_number == 2:
        team_output = Bandits
        team_name = "Bandits"
    elif team_number == 3:
        team_output = Warriors
        team_name = "Warriors"
    else:
        print("Invalid input. Please pick a number 1-3.")

    for player in team_output:
        if player.get("experience") == True:
            experienced_players += 1
        else:
            inexperienced_players += 1
        total_height = player.get("height") + total_height

    total_players = len(team_output)
    average_height = total_height / total_players

    print(f"\nTeam: {team_name} Stats")
    print("--------------------")
    print(f"Total players: {total_players}")
    print(f"Total experienced: {experienced_players}")
    print(f"Total inexperienced: {inexperienced_players}")
    print(f"Average height: {average_height}\n")

    print("\nPlayers on Team:")
    for player in team_output:
        print(player.get("name"), end=", ")
    print()

    print("\nGuardians:")
    for guardian in team_output:
        print(guardian.get("guardians"), end=", ")
    print()


if __name__ == '__main__':
    clean_data()
    balance_teams()
    display_options()
    while True:
        try:
            user_input = int(input("Enter an Option: "))
        except:
            print("Invalid Input. Please enter a 1 or a 2.")
        else:
            if user_input == 1:
                display_team_options()
                team_input = int(input("Enter an Option: "))
                display_team_stats(team_input)
                break
            elif user_input == 2:
                print("Thank you. Please come back again.")
                break
            else:
                print("Invalid Input. Please enter a 1 or a 2.")
                continue
