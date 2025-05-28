from faker import Faker
from models import Expense , session

faker = Faker()

for _ in range (10):
    expense = Expense(
        name=faker.name(),
        amount=faker.random_int(min=100, max=1000)
    )
    session.add(expense)
session.commit()
print("seeded database with 10 expenses.")
