import ipdb

def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

######### HELPER FUNCTIONS ###########

def get_all_players():
    home_team = game_dict()['home']['players']
    away_team = game_dict()['away']['players']
    all_players = home_team + away_team
    return all_players

def get_both_teams():
    home_team = [game_dict()['home']]
    away_team = [game_dict()['away']]
    both_teams = home_team + away_team
    return both_teams

##########################################

def num_points_per_game(name):
    for player in get_all_players():
        if player['name'] == name:
            return player['points_per_game'] 

def player_age(name):
    for player in get_all_players():
        if player['name'] == name:
            return player['age']
            
def team_colors(team_name):
    # CLASSIC FOR LOOP VERSION
    for team in get_both_teams():
        if team['team_name'] == team_name:
            return team["colors"]
    
    # LIST EXPRESSION VERSION
    # return [color for team in get_both_teams() if team["team_name"] == team_name for color in team["colors"]]

def team_names():
    # CLASSIC FOR LOOP VERSION
    teams = []
    for home_or_away in game_dict():
        for info in game_dict()[home_or_away]:
            if info == "team_name":
                teams.append(game_dict()[home_or_away][info])
    return teams

 # LIST EXPRESSION VERSION
    # return [game_dict()[home_or_away][info] for home_or_away in game_dict() for info in game_dict()[home_or_away] if info == "team_name"]


def player_numbers(team_name):
    numbers = []
    for team in game_dict():
        home_or_away = game_dict()[team]
        for info in home_or_away:
            current_team_name = game_dict()[team][info]
            if current_team_name == team_name:
                list_of_players = game_dict()[team]["players"]
                for player in list_of_players:
                    numbers.append(player["number"])
    return numbers


def player_stats(player_name):
    stats = {}
    for team in game_dict():
        home_or_away = game_dict()[team]
        for info in home_or_away:
            if info == "players":
                current_team_players = game_dict()[team][info]
                for player in current_team_players:
                    if player["name"] == player_name:
                        stats.update(player)
    return stats


########CHALLENGE#########


def average_rebounds_by_shoe_brand():
    average_rebounds_by_brand = {}
    
    # Populate average_rebounds_by_brand
    for team in game_dict():
        home_or_away = game_dict()[team]
        for info in home_or_away:
            if info == "players":
                current_team_players = game_dict()[team][info]
                for player in current_team_players:
                    brand = player["shoe_brand"]
                    rebounds = player["rebounds_per_game"]
                    if brand not in average_rebounds_by_brand:
                        average_rebounds_by_brand[brand] = [rebounds]
                    else:
                        average_rebounds_by_brand[brand].append(rebounds)          
    
    #Initialize Rounded version of average_rebounds_by_brand
    rounded_average_rebounds_by_brand = {}

    # Iterate through average_rebounds_by_brand
    for brand in average_rebounds_by_brand:
        list_of_rebounds = average_rebounds_by_brand[brand]
        sum_of_rebounds = sum(list_of_rebounds) # Sum the list up
        average_rebounds = sum_of_rebounds / len(list_of_rebounds) # Calculate average of list
        rounded_average_rebounds = round(average_rebounds, 2) # Round to two decimal places
        rounded_average_rebounds_by_brand[brand] = rounded_average_rebounds 

    # Update average_rebounds_by_brand
    average_rebounds_by_brand.update(rounded_average_rebounds_by_brand)     

    # Convert average_rebounds_by_brand to String
    to_string = "\n".join(f"{key}:  {value:.2f}" for key, value in average_rebounds_by_brand.items())
    
    return to_string       

print(average_rebounds_by_shoe_brand())