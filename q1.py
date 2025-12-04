import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    # Using Distinct because we only want to return one appearance of each driver
    cursor.execute("""
        SELECT DISTINCT Driver
        FROM drivers_updated
        WHERE Nationality = 'BRA'
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))