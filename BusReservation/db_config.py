import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",               # Replace with your MySQL host
            user="root",                    # Replace with your MySQL username
            password="Sakshi@01",           # Replace with your MySQL password
            database="Project"              # Replace with your MySQL database name
        )
        if connection.is_connected():
            print("Successfully connected to the database!")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

if __name__ == "__main__":
    # Test the database connection
    conn = get_db_connection()
    if conn:
        # Close the connection after checking
        conn.close()
        print("Connection closed.")
    else:
        print("Failed to connect to the database.")

    
