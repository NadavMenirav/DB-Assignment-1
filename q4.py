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
    # First, I created a CTE that finds which car had the most wins in 1999.
    # I grouped the winners by car, sorted them by the number of wins,
    # and used LIMIT 1 to take the car with the highest count.
    #
    # Then, in the main query, I joined the winners table with that CTE
    # and counted how many wins that same car had in the year 2001.

    cursor.execute("""
        WITH bestCarIn1999 AS (	
            SELECT w.Car AS car
            FROM winners w
            WHERE YEAR(w.Date) = 1999
            GROUP BY w.Car
            ORDER BY COUNT(*) DESC
            LIMIT 1
        )
        SELECT Count(*)
        FROM winners w, bestCarIn1999 b
        WHERE YEAR(w.Date) = 2001 AND w.Car = b.car
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()