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

    # First, I created two CTEs: ferrariPoints and maseratiPoints.
    # Each CTE calculates the total points for the respective team by summing the PTS column in teams_updated.
    # Then, in the main query, I subtract Maserati's total points from Ferrari's total points
    # and label the result as diff.

    cursor.execute("""
        WITH ferrariPoints AS (
	        SELECT SUM(PTS) Sum
	        FROM teams_updated
	        WHERE Car = 'Ferrari'
        ),
        maseratiPoints AS (
	        SELECT SUM(PTS) Sum
            FROM teams_updated
            WHERE Car = 'Maserati'
        )

        SELECT f.Sum - m.Sum diff
        FROM ferrariPoints f, maseratiPoints m

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()