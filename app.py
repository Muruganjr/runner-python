import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

# MySQL Connection Configuration
config = {
    'user': 'root',
    'password': 'password',  # Change as per your MySQL setup
    'host': 'mysql-db',  # The hostname or IP address of the MySQL service
    'database': 'testdb',
}

@app.route('/')
def insert_and_fetch_data():
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Create table if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")

        # Insert Data
        cursor.execute("INSERT INTO users (name) VALUES ('Murugan')")
        connection.commit()

        # Fetch Data
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()

        return jsonify(result)

    except mysql.connector.Error as err:
        return f"Error: {err}"

    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
