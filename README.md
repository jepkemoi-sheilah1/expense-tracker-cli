#  Expense Tracker CLI App

This is a simple command-line app built in Python that allows users to track their expenses using an SQLite database and SQLAlchemy ORM.

## Features

- List all expenses
- Add a new expense
- Seed the database with fake data

## File Structure

- `cli.py`: The main entry point for the CLI.
- `models.py`: Contains SQLAlchemy model definitions.
- `helpers.py`: Contains helper functions used by the CLI.
- `seed.py`: Seeds the database with fake data using Faker.
- `db/migrations/`: Contains Alembic migration files.

## Running the App

1. Install dependencies:
    ```bash
    pipenv install
    pipenv shell
    ```

2. Seed the database:
    ```bash
    python lib/seed.py
    ```

3. Run the CLI:
    ```bash
    python lib/cli.py
    ```

---

