#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed.
"""
import MySQLdb
import sys


def main():
    """
    Connects to a MySQL database and retrieves states based on user input.
    Arguments:
        sys.argv[1]: MySQL username
        sys.argv[2]: MySQL password
        sys.argv[3]: Database name
        sys.argv[4]: State name to search for
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> "
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

        if not rows:
            print(f"No state found with name '{state_name}'")
        else:
            for row in rows:
                print(row)

    except MySQLdb.Error as e:
        print(f"Error executing SQL query: {e}")

    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
