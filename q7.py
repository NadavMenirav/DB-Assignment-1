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

    # This query finds all drivers who either won a race driving Ferrari or have Argentine nationality.
    # The first part selects distinct winners who drove Ferrari, and the second part selects distinct drivers from Argentina.
    # UNION combines both sets and removes duplicates, and ORDER BY driver sorts the final result alphabetically.

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