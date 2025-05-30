from models import session, User, Category, Expense, Total
# This module provides helper functions for managing users, categories, expenses, and totals in the application.
def list_users():
    users = User.get_all(session)
    for u in users:
        print(f"{u.id}. {u.name}")

def create_user():
    name = input("Enter user name: ")
    user = User.create(session, name)
    print(f"User created with ID: {user.id}")

def delete_user():
    user_id = int(input("Enter user ID to delete: "))
    if User.delete(session, user_id):
        print("User deleted.")
    else:
        print("User not found.")

def list_categories():
    categories = Category.get_all(session)
    for c in categories:
        print(f"{c.id}. {c.name}")

def create_category():
    from datetime import datetime
    name = input("Enter category name: ")
    budget_input = input("Enter budget for this category (default 0.0): ")
    try:
        budget = float(budget_input)
        if budget < 0:
            print("Budget cannot be negative. Setting to 0.0")
            budget = 0.0
    except ValueError:
        print("Invalid budget input. Setting to 0.0")
        budget = 0.0
    category = Category.create(session, name, budget)
    print(f"Category created with ID: {category.id} with budget ${budget:.2f}")

def get_total_spent_for_category_month(category_id, year=None, month=None):
    from datetime import datetime
    from sqlalchemy import func, extract
    if year is None or month is None:
        today = datetime.today()
        year = today.year
        month = today.month
    total_spent = session.query(func.sum(Expense.amount)).filter(
        Expense.category_id == category_id,
        extract('year', Expense.date) == year,
        extract('month', Expense.date) == month
    ).scalar()
    return total_spent or 0.0

def list_categories():
    from datetime import datetime
    categories = Category.get_all(session)
    if not categories:
        print("No categories found.")
        return
    today = datetime.today()
    print("Categories:")
    for c in categories:
        total_spent = get_total_spent_for_category_month(c.id, today.year, today.month)
        remaining = c.budget - total_spent
        print(f"{c.id}. {c.name} - Budget: ${c.budget:.2f}, Spent: ${total_spent:.2f}, Remaining: ${remaining:.2f}")

def delete_category():
    category_id = int(input("Enter category ID to delete: "))
    if Category.delete(session, category_id):
        print("Category deleted.")
    else:
        print("Category not found.")

def list_expenses():
    expenses = Expense.get_all(session)
    for e in expenses:
        category_name = e.category.name if e.category else "No Category"
        print(f"{e.id}. {e.description} - ${e.amount} - Category: {category_name}")

def add_expense():
    from datetime import datetime, date as date_class
    description = ""
    while not description.strip():
        description = input("Enter expense description (required): ")
        if not description.strip():
            print("Description cannot be empty. Please enter a valid description.")
    amount = None
    while amount is None:
        try:
            amount_input = input("Enter amount: ")
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero.")
                amount = None
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    # Show categories for user to select
    categories = Category.get_all(session)
    if not categories:
        print("No categories found. Please create a category first.")
        return
    print("Select a category from the list:")
    for c in categories:
        print(f"{c.id}. {c.name}")
    category_id = None
    while category_id is None:
        category_input = input("Enter category ID: ")
        try:
            category_id_int = int(category_input)
            if any(c.id == category_id_int for c in categories):
                category_id = category_id_int
            else:
                print("Invalid category ID. Please select from the list.")
        except ValueError:
            print("Invalid input. Please enter a numeric category ID.")
    # Automatically set date to today
    date = date_class.today()
    user_id_input = input("Enter user ID or leave blank: ")
    user_id = int(user_id_input) if user_id_input else None
    expense = Expense.create(session, amount=amount, description=description, date=date, user_id=user_id, category_id=category_id)
    print(f"Expense added with ID: {expense.id}")

def get_total_expenses_by_user():
    from sqlalchemy import func
    totals = session.query(
        User.name,
        func.sum(Expense.amount)
    ).join(Expense, Expense.user_id == User.id).group_by(User.id).all()
    if not totals:
        print("No expenses found.")
        return
    print("Total expenses by user:")
    for name, total in totals:
        print(f"{name}: ${total:.2f}")

def get_total_expenses_by_category():
    from sqlalchemy import func
    totals = session.query(
        Category.name,
        func.sum(Expense.amount)
    ).join(Expense, Expense.category_id == Category.id).group_by(Category.id).all()
    if not totals:
        print("No expenses found.")
        return
    print("Total expenses by category:")
    for name, total in totals:
        print(f"{name}: ${total:.2f}")

def delete_expense():
    expense_id = int(input("Enter expense ID to delete: "))
    if Expense.delete(session, expense_id):
        print("Expense deleted.")
    else:
        print("Expense not found.")

def list_totals():
    totals = Total.get_all(session)
    for t in totals:
        print(f"{t.id}. Month: {t.month}, Total Amount: {t.total_amount}")

def create_total():
    month = input("Enter month (YYYY-MM): ")
    total_amount_input = input("Enter total amount or leave blank: ")
    total_amount = float(total_amount_input) if total_amount_input else 0.0
    user_id_input = input("Enter user ID or leave blank: ")
    user_id = int(user_id_input) if user_id_input else None
    total = Total.create(session, month=month, total_amount=total_amount, user_id=user_id)
    print(f"Total created with ID: {total.id}")

def delete_total():
    total_id = int(input("Enter total ID to delete: "))
    if Total.delete(session, total_id):
        print("Total deleted.")
    else:
        print("Total not found.")

def update_category_budget():
    category_id = int(input("Enter category ID to update budget: "))
    category = Category.find_by_id(session, category_id)
    if not category:
        print("Category not found.")
        return
    budget_input = input(f"Enter new budget for category '{category.name}' (current: ${category.budget:.2f}): ")
    try:
        new_budget = float(budget_input)
        if new_budget < 0:
            print("Budget cannot be negative. Update cancelled.")
            return
    except ValueError:
        print("Invalid budget input. Update cancelled.")
        return
    category.budget = new_budget
    session.commit()
    print(f"Budget for category '{category.name}' updated to ${new_budget:.2f}")
