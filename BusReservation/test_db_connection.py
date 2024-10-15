from db_config import get_db_connection

if __name__ == "__main__":
    # Test the database connection
    conn = get_db_connection()
    if conn:
        # Close the connection after checking
        conn.close()
        print("Connection closed.")
    else:
        print("Failed to connect to the database.")
