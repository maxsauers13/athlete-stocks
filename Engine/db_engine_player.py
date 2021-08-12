import sql_connection

# inserts a player record into the mysql database
def insert_player(name, price):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "INSERT INTO players (playerName, playerPrice) VALUES (%s, %s)"
    parameters = (name, str(price))

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records inserted.")

# gets a player record from the mysql database
def get_player(name):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "SELECT * FROM players WHERE playerName = %s"
    parameters = (name, )

    db_controller.execute(query, parameters)
    players = db_controller.fetchall()

    for player in players:
        print(player)

# updates a player record from the mysql database
def update_playerPrice(name, price):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "UPDATE players SET playerPrice = %s WHERE playerName = %s"
    parameters = (str(price), name)

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records affected.")

# delete a player record from the mysql database
def delete_player(name):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "DELETE FROM players WHERE playerName = %s"
    parameters = (name, )

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records deleted.")