import sqlite3


def initialize_database():
# # 1. Establish a connection (creates the file if it does not exist)
# conn = sqlite3.connect("my_database.db")
    connection = sqlite3.connect("my_database.db")
    # # 2. Create a cursor object to execute commands
    cursor = connection.cursor()



    # 3. Execute SQL commands

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (   
                
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                interests TEXT,
                created_at DATE DEFAULT CURRENT_DATE
            )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (   
                
                article_id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                source TEXT NOT NULL,
                publication_date DATE NOT NULL
            )
    """)



    # 4. Commit structural or data mutations
    connection.commit()

    # 5. Terminate the connection when finished
    connection.close()







