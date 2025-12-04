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
    # We query for all the best laps of every driver in the year 2,000
    # Group them by the driver, in order to find the best lap
    # and then join the best lap of each driver with all the winners in order to ascertain that
    # the driver also won at least one race, and completed the most laps.

    cursor.execute("""
        SELECT 	w.Winner as 'driver name', gl.min_time
        FROM 	f1_data.winners as w JOIN (
                                            SELECT l.Driver, MIN(l.Time) as min_time, l.year
                                            FROM f1_data.fastest_laps_updated as l
                                            WHERE l.year = 2000
                                            GROUP BY l.Driver, l.year
                                            ) as gl
               ON (w.Winner = gl.Driver AND YEAR(w.Date) = gl.year)
               GROUP BY w.Winner
               HAVING   SUM(w.Laps) >= ALL(
                   SELECT SUM(Laps)
                   FROM f1_data.winners
                   WHERE YEAR(Date) = 2000
                   GROUP BY (Winner))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()