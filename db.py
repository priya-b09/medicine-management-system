import mysql.connector
print("hello")
def get_connection():
    try:
        print("im priya")
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="priya@2006",
            database="medicine_db"
        )
     
        if conn.is_connected():
            print("Connected to the database")

        return conn

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        pass