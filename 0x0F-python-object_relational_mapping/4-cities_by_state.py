#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa sorted
in ascending order.
"""

import MySQLdb
import sys


def main():
    """
    Connects to database and retrieves cities with their states.
    """

    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <username> <password> "
              "<database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()

        query = """
            Select cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error executing query: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
