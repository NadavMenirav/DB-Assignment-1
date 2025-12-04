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

    cursor.execute("""
        SELECT DISTINCT Winner driver
        FROM winners 
        WHERE Car = 'Ferrari'

        UNION 

        SELECT DISTINCT Driver driver
        FROM drivers_updated
        WHERE Nationality = 'ARG'

        ORDER BY driver
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()