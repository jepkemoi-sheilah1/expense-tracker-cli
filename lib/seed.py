from faker import Faker
from models import Expense, session
from datetime import date
import random

faker = Faker()

for _ in range(10):
    expense = Expense(
        amount=faker.random_int(min=100, max=1000),
        description=faker.sentence(nb_words=6),
        date=date.today(),
        user_id=random.randint(1, 5),
        category_id=random.randint(1, 5)
    )
    session.add(expense)
session.commit()
print("seeded database with 10 expenses.")
