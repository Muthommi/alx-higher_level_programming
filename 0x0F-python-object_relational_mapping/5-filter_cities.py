#!/usr/bin/python3
"""
This script lists all cities of a given state from the database.
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySql database and retrieves cities of a given state.
    """
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> "
              "<database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()

        query = (
            "SELECT GROUP_CONCAT"
            "(cities.name ORDER BY cities.id ASC SEPARATOR ', ') "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s"
        )
        cursor.execute(query, (state_name,))

        result = cursor.fetchone()

        if result:
            print(result[0])

    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
