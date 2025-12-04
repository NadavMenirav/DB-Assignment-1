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

    # First, I created a CTE called fastLaps to select all cars whose fastest lap time
    # was under 2 minutes. I grouped by car and used MIN to check the fastest time per car.
    #
    # Then, in the main query, I joined this CTE with the teams_updated table to get points.
    # I calculated the average points per car, grouped by car, and sorted the results
    # in descending order. The query returns the car name and the average points as avg_pts.

    cursor.execute("""
        WITH fastLaps AS (
	        SELECT DISTINCT f.Car as Car
            FROM fastest_laps_updated f
            GROUP BY f.Car
            HAVING MINUTE(STR_TO_DATE(MIN(f.Time), '%i:%s.%f')) < 2
        )

        SELECT f.Car 'car name', AVG(t.PTS) avg_pts
        FROM fastLaps f JOIN teams_updated t ON f.Car = t.Car
        GROUP BY t.Car
        ORDER BY avg_pts DESC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()