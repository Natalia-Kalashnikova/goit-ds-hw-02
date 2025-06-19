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
        # читаємо файл зі скриптом для створення БД
        with open("schema.sql", "r", encoding="utf-8") as f:
            sql = f.read()

        # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
        with sqlite3.connect("task_manager.db") as con:
            cur = con.cursor()
            # виконуємо скрипт із файлу, який створить таблиці в БД
            cur.executescript(sql)

            print("Database created successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred while creating the database: {e}")


if __name__ == "__main__":
    create_db()
