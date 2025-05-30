from helpers import (
    list_users, create_user, delete_user,
    list_categories, create_category, delete_category,
    list_expenses, add_expense, delete_expense,
    list_totals, create_total, delete_total,
    get_total_expenses_by_user, get_total_expenses_by_category, update_category_budget
)

def main():
    print("Welcome to the Expense Tracker CLI")
    while True:
        print("\n Select an option:")
        print("1. Users")
        print("2. Categories")
        print("3. Expenses")
        print("4. Totals")
        print("5. Budget Planning")
        print("6. Quit")
        choice = input("> ")
        if choice == "1":
            user_menu()
        elif choice == "2":
            category_menu()
        elif choice == "3":
            expense_menu()
        elif choice == "4":
            total_menu()
        elif choice == "5":
            budget_planning_menu()
        elif choice == "6":
            print("Thank you for using the Expense Tracker CLI. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. List Users")
        print("2. Create User")
        print("3. Delete User")
        print("4. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_users()
        elif choice == "2":
            create_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def category_menu():
    while True:
        print("\nCategory Menu:")
        print("1. List Categories")
        print("2. Create Category")
        print("3. Delete Category")
        print("4. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_categories()
        elif choice == "2":
            create_category()
        elif choice == "3":
            delete_category()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def expense_menu():
    print("Please select an option ")
    while True:
        print("\nExpense Menu:")
        print("1. List Expenses")
        print("2. Add Expense")
        print("3. Delete Expense")
        print("4. View Total Expenses by User")
        print("5. View Total Expenses by Category")
        print("6. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            get_total_expenses_by_user()
        elif choice == "5":
            get_total_expenses_by_category()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

def total_menu():
    while True:
        print("\nTotal Menu:")
        print("1. List Totals")
        print("2. Create Total")
        print("3. Delete Total")
        print("4. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_totals()
        elif choice == "2":
            create_total()
        elif choice == "3":
            delete_total()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

def budget_planning_menu():
    while True:
        print("\nBudget Planning Menu:")
        print("1. View Budgets and Spending")
        print("2. Update Category Budget")
        print("3. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            list_categories()
        elif choice == "2":
            update_category_budget()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
