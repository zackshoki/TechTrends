import database
import sqlite3

def create_user(username):
    # connection = sqlite3.connect("my_database.db")
    connection = sqlite3.connect("my_database.db")
    # # 2. Create a cursor object to execute commands
    cursor = connection.cursor()
    #  insert new user into database
    cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
    # commit change
    connection.commit()
    # grab a new row
    new_id = cursor.lastrowid
    #  close connection
    connection.close()
    # return new row
    return new_id


def save_user_interest_database(user_id, interests):
    connection = sqlite3.connect("my_database.db")
    # # 2. Create a cursor object to execute commands
    cursor = connection.cursor()
    # update users interests in the database
    cursor.execute("UPDATE users SET interests = ? WHERE user_id = ?", (interests, user_id))
    # commit change
    connection.commit()
    connection.close()





# get_user_interests(user_id)


# get_user(username):
#     # # 1. Establish a connection (creates the file if it does not exist)
#     # conn = sqlite3.connect("my_database.db")
#     connection = sqlite3.connect("my_database.db")
#     # # 2. Create a cursor object to execute commands
#     cursor = connection.cursor()
#     # select user from database
#     cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#     # dave matching result or return None
#     row = cursor.fetchlone()