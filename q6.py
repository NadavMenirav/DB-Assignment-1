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

    # We are looking for all pairs of different Grand Prix events that had the same number of laps.
    # First, we consider only races with 80 laps or more.
    # Then, we join the winners table with itself to find pairs where the number of laps is equal.
    # To make sure each pair appears only once and GP1 comes before GP2 alphabetically,
    # we use the condition a.`Grand Prix` < b.`Grand Prix`.
    # Finally, we select the GP names as GP1 and GP2, and the number of laps.

    cursor.execute("""
        SELECT DISTINCT a.`Grand Prix` GP1, b.`Grand Prix` GP2, a.Laps Laps
        FROM winners a, winners b
        WHERE a.Laps = b.Laps
        AND a.Laps >= 80
        AND a.`Grand Prix` < b.`Grand Prix`
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()