#!/usr/bin/python3
"""
This script displays all values in the states table hbtn_0e_0_usa
where the name matches the argument passed.
"""

import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves states based on user input.
    """

    if len(sys.argv) != 5:
        print("usage: ./3-my_safe_filter_states.py <username> <password> "
              "<database_name> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    try:
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")

    finally:
        cursor.close
        db.close()


if __name__ == "__main__":
    main()
