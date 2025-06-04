# Expense Tracker CLI App

## link to Expense-Tracker-CLI schema 
```
https://dbdiagram.io/d/Expense-Tracker-Application-683451b16980ade2eb6776d1

```
## link to demo video 

C:\Users\HP\OneDrive\Documents\Zoom\2025-05-31 22.24.38 jepkemoi sheilah's Zoom Meeting


This is a simple command-line app built in Python that allows users to track their expenses using an SQLite database and SQLAlchemy ORM. The Expense Tracker helps users budget and track their expenses by allowing them to add, view, and delete expenses. It empowers users to create budgets for specific categories, log daily expenses, and track spending against their limits.

## Features

- List all expenses
- Add a new expense
- Delete an expense
- View totals by category or user
- Budget Planning: View budgets and spending per category, update category budgets

## Directory Structure

- `lib/cli.py`: The main entry point for the CLI. Handles user interaction, menu display, and input processing.
- `lib/helpers.py`: Contains helper functions used by the CLI to perform operations such as adding or listing expenses and managing budgets.
- `lib/models.py`: Contains SQLAlchemy model definitions representing the data structures for users, categories, expenses, and totals.
- `lib/seed.py`: Seeds the database with fake data using the Faker library to facilitate testing and development.
- `lib/app.db/`: Contains the SQLite database file and Alembic migration files for managing database schema changes.

## Getting Started

### Environment Setup

Install dependencies and activate the virtual environment:

```bash
pipenv install
pipenv shell
```

### Database Setup

Seed the database with initial data:

```bash
python lib/seed.py
```

### Running the CLI

Start the CLI application:

```bash
python lib/cli.py
```

Follow the on-screen prompts to navigate through the menu options for managing users, categories, expenses, viewing totals, and budget planning.

## Testing

Manual testing is recommended by running the CLI and interacting with the menu options to verify functionality such as adding, listing, deleting expenses, and managing budgets.

## Support / Contact

For support or inquiries, please contact the project owner.

## License

This project is licensed under the MIT License.

# owner
GitHub account : jepkemoi-sheilah1
Email : jepkemoishyllah@gmail.com 



