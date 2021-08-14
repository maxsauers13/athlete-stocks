import PlayerEngine.data_getter
import json

# returns a list of tuples containing player names and their corresponding prices
def evaluate_league():
    league_json = PlayerEngine.data_getter.get_API_data()
    #Load JSON string into a dictionary
    league_dict = json.loads(league_json)

    player_prices = []

    for player in league_dict:
        price = price_player_stock(player)
        name = player["Name"]
        player_prices.append((name, price))

    return player_prices

# calculates and returns the stock price of a player
def price_player_stock(player_dict):
    games_played = player_dict["Games"]

    if games_played == 0:
        return 0

    avg_points = player_dict["Points"] / games_played
    avg_assists = player_dict["Assists"] / games_played
    avg_rebounds = player_dict["Rebounds"] / games_played
    avg_steals = player_dict["Steals"] / games_played
    avg_blocks = player_dict["BlockedShots"] / games_played
    avg_turnovers = player_dict["Turnovers"] / games_played

    player_price = avg_points + avg_assists + avg_rebounds + avg_steals + avg_blocks - avg_turnovers
    player_price = round(player_price, 2)
    return player_price