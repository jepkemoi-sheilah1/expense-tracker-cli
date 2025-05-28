from helpers import list_expenses, add_expense

def main():
    print("Welcome to the Expense Tracker CLI")
    while True:
        print("\nOptions:\n1. List Expenses\n2. Add Expense\n3. Quit")
        choice = input("> ")
        if choice == "1":
            list_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
