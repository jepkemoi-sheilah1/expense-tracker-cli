from models import session, Expense

def list_expenses():
    expenses = session.query(Expense).all()
    for e in expenses:
        print(f"{e.id}. {e.description} - ${e.amount}")

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount: "))
    expense = Expense(description=description, amount=amount)
    session.add(expense)
    session.commit()
    print("Expense added!")
