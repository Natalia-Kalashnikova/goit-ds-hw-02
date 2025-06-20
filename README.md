# Task Manager SQLite Project

This project implements a task management system database using SQLite and Python.

---

## Project Structure

- `schema.sql` — SQL script to create database tables.
- `create_db.py` — Script to create the database and tables.
- `seed.py` — Script to populate the database with fake data using Faker.
- `queries.py` — Example SQL queries for common operations.
- `task_manager.db` — SQLite database file (created after running scripts).

---

## Setup Instructions

1. Install dependencies with Poetry:

```bash
poetry install
```

2. Create the database and tables:

```bash
poetry python create_db.py
```

3. Populate the database with sample data:

```bash
poetry python seed.py
```

---

## Usage

- Modify `schema.sql` to change database schema.
- Use `queries.py` or your own scripts to interact with the database.
- The database file `task_manager.db` is created automatically.
- Foreign key constraints are enabled.

## Notes

- Remember to add `task_manager.db` to `.gitignore` to avoid committing the database file.
- Use parameterized queries to prevent SQL injection.

## License

MIT License.

---
