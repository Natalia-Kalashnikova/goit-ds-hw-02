"""
Module to seed the SQLite database with sample data.

This script populates the 'status', 'users', and 'tasks' tables
in the database located at 'task_manager.db' using Faker for fake data.
"""

import random
import sqlite3
from faker import Faker

DB_PATH = "task_manager.db"
fake = Faker()


def seed_statuses():
    """Insert predefined statuses into the status table."""
    statuses = ["new", "in progress", "completed"]
    try:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.executemany(
                "INSERT INTO status (name) VALUES (?)", [(s,) for s in statuses]
            )
            con.commit()
    except sqlite3.Error as e:
        print(f"Error inserting statuses: {e}")
        raise


def seed_users(num_users=20):
    """Insert fake users into the users table.

    Args:
        num_users (int): Number of fake users to create.
    """
    users = [(fake.name(), fake.unique.email()) for _ in range(num_users)]
    try:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", users)
            con.commit()
    except sqlite3.Error as e:
        print(f"Error inserting users: {e}")
        raise


def seed_tasks(num_tasks=60):
    """Insert fake tasks into the tasks table.

    Args:
        num_tasks (int): Number of fake tasks to create.
    """
    try:
        with sqlite3.connect(DB_PATH) as con:
            cur = con.cursor()
            cur.execute("SELECT id FROM users")
            user_ids = [row[0] for row in cur.fetchall()]
            cur.execute("SELECT id FROM status")
            status_ids = [row[0] for row in cur.fetchall()]

            tasks = []
            for _ in range(num_tasks):
                title = fake.sentence(nb_words=6)
                description = fake.text() if random.random() > 0.2 else None
                status_id = random.choice(status_ids)
                user_id = random.choice(user_ids)
                tasks.append((title, description, status_id, user_id))

            cur.executemany(
                "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
                tasks,
            )
            con.commit()
    except sqlite3.Error as e:
        print(f"Error inserting tasks: {e}")
        raise


def seed_all():
    """Run all seed functions to populate the database."""
    try:
        seed_statuses()
        seed_users()
        seed_tasks()
        print("Database seeded successfully.")
    except sqlite3.Error as e:
        print(f"Seeding failed due to database error: {e}")


if __name__ == "__main__":
    seed_all()
