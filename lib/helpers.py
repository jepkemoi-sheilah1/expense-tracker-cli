from models import session, Expense

def list_expenses():
    expenses = session.query(Expense).all()
    for e in expenses:
        print(f"{e.id}. {e.name} - ${e.amount}")

def add_expense():
    name = input("Enter expense name: ")
    amount = int(input("Enter amount: "))
    expense = Expense(name=name, amount=amount)
    session.add(expense)
    session.commit()
    print("Expense added!")
