#!/usr/bin/python3
"""
This script lists all states with a name starting with N from the database
hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def main():
    """
    It connects to a MySQL database and retrieves all states starting with 'N'
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
