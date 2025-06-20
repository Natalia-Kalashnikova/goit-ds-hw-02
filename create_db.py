"""
Create SQLite database and tables by executing SQL commands from schema.sql file.

Reads the SQL schema from 'schema.sql', connects to (or creates) 'task_manager.db',
and executes the SQL script to create necessary tables. Enables foreign key support.

Prints a success message if the database is created successfully,
or an error message if an exception occurs during execution.
"""

import sqlite3


def create_db():
    """
    Create SQLite database and tables by executing SQL commands from schema.sql file.

    Reads the SQL schema from 'schema.sql', connects to (or creates) 'task_manager.db',
    and executes the SQL script to create necessary tables. Enables foreign key support.

    Prints a success message if the database is created successfully,
    or an error message if an exception occurs during execution.
    """
    try:
        # read the file with the script to create the database
        with open("schema.sql", "r", encoding="utf-8") as f:
            sql = f.read()

        # create a connection to the database (if the database file does not exist, it will be created)
        with sqlite3.connect("task_manager.db") as con:
            cur = con.cursor()
            # execute a script from a file that will create tables in the database
            cur.executescript(sql)

            print("Database created successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred while creating the database: {e}")


if __name__ == "__main__":
    create_db()
