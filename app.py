import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='mysql',  # Since MySQL runs in Docker, use the container name as host
            user='root',
            password='rootpassword',
            database='test_db'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")
    connection.commit()

def insert_data(connection, name, age):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    connection.commit()

def select_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    connection = create_connection()
    if connection:
        create_table(connection)
        insert_data(connection, "John", 30)
        insert_data(connection, "Jane", 25)
        select_data(connection)
        connection.close()

if __name__ == "__main__":
    main()
