import DatabaseEngine.sql_connection

# updates a player record from the mysql database
def update_playerPrices_table(players):
    db_connection = DatabaseEngine.sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "UPDATE players SET playerPrice = %s WHERE playerName = %s"

    for player in players:
        parameters = (player[1], player[0])
        db_controller.execute(query, parameters)
        db_connection.commit()

    print("Prices updated.")

# inserts a player record into the mysql database
def insert_players_table(players):
    db_connection = DatabaseEngine.sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "INSERT INTO players (playerName, playerPrice) VALUES (%s, %s)"

    for player in players:
        parameters = (player[0], player[1])
        db_controller.execute(query, parameters)
        db_connection.commit()

    print("Records inserted.")

# delete a player record from the mysql database
def clear_players_table():
    db_connection = DatabaseEngine.sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "DELETE FROM players"

    db_controller.execute(query)
    db_connection.commit()

    print("Table cleared.")