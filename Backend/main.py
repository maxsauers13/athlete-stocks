import DatabaseEngine.db_engine_player
import PlayerEngine.player_pricing

def main():
    
    # get the most updated player prices
    player_prices = PlayerEngine.player_pricing.evaluate_league()

    # insert the player prices into the database -- only do this to initialize players in the database, otherwise update
    # DatabaseEngine.db_engine_player.insert_players_table(player_prices)

    # update the player prices in the database
    DatabaseEngine.db_engine_player.update_playerPrices_table(player_prices)

    # clear the player table
    # DatabaseEngine.db_engine_player.clear_players_table()

main()