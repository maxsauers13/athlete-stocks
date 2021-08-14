import DatabaseEngine.sql_connection

# inserts a user record into the mysql database
def insert_user(username, balance):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "INSERT INTO userAccounts (username, totalbalance) VALUES (%s, %s)"
    parameters = (username, str(balance))

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records inserted.")

# gets a user record from the mysql database
def get_user(username):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "SELECT * FROM userAccounts WHERE username = %s"
    parameters = (username, )

    db_controller.execute(query, parameters)
    users = db_controller.fetchall()

    for user in users:
        print(user)

# updates a user record from the mysql database
def update_totalbalance(username, balance):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "UPDATE userAccounts SET totalbalance = %s WHERE username = %s"
    parameters = (str(balance), username)

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records affected.")

# delete a user record from the mysql database
def delete_user(username):
    db_connection = sql_connection.connection()
    db_controller = db_connection.cursor()

    query = "DELETE FROM userAccounts WHERE username = %s"
    parameters = (username, )

    db_controller.execute(query, parameters)
    db_connection.commit()

    print(db_controller.rowcount, "records deleted.")