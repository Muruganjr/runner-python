import mysql.connector

# Define the connection parameters
config = {
    'user': 'root',
    'password': 'password',  # MySQL root password
    'host': 'localhost',     # Host is 'localhost' since MySQL runs on the same instance
    'port': '3306',          # MySQL default port
    'database': 'testdb'     # The database created during the Docker run
}

def insert_data(name):
    try:
        # Establish the MySQL connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Create table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
        """)

        # Insert data into the table
        insert_query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(insert_query, (name,))
        connection.commit()
        print(f"Data inserted: {name}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

def fetch_data():
    try:
        # Establish the MySQL connection
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Fetch data from the table
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        # Print the fetched data
        for row in rows:
            print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    # Insert sample data
    insert_data('Murugan')

    # Fetch and display the data
    print("Fetched Data:")
    fetch_data()
