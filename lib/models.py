from sqlalchemy import Column, Integer, String, create_engine, Float, ForeignKey, Date, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
    totals = relationship("Total", back_populates="user", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def delete(cls, session, user_id):
        user = session.query(cls).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).get(user_id)

    def __repr__(self):
        return f"<User id={self.id} name={self.name}>"

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    budget = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    expenses = relationship("Expense", back_populates="category", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, name, budget=0.0):
        category = cls(name=name, budget=budget)
        session.add(category)
        session.commit()
        return category

    @classmethod
    def delete(cls, session, category_id):
        category = session.query(cls).get(category_id)
        if category:
            session.delete(category)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, category_id):
        return session.query(cls).get(category_id)

    def __repr__(self):
        return f"<Category id={self.id} name={self.name}>"

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    description = Column(String)
    date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user_id = Column(Integer, ForeignKey('users.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    print("you added a new expense")
   # print("your total expenses are now updated")

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    @classmethod
    def create(cls, session, amount, description=None, date=None, user_id=None, category_id=None):
        expense = cls(amount=amount, description=description, date=date, user_id=user_id, category_id=category_id)
        session.add(expense)
        session.commit()
        return expense

    @classmethod
    def delete(cls, session, expense_id):
        expense = session.query(cls).get(expense_id)
        if expense:
            session.delete(expense)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, expense_id):
        return session.query(cls).get(expense_id)

    def __repr__(self):
        return f"<Expense id={self.id} amount={self.amount} user_id={self.user_id} category_id={self.category_id}>"

class Total(Base):
    __tablename__ = 'totals'

    id = Column(Integer, primary_key=True)
    month = Column(String, nullable=False)  # e.g. '2025-05'
    total_amount = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="totals")

    @classmethod
    def create(cls, session, month, total_amount=0.0, user_id=None):
        total = cls(month=month, total_amount=total_amount, user_id=user_id)
        session.add(total)
        session.commit()
        return total

    @classmethod
    def delete(cls, session, total_id):
        total = session.query(cls).get(total_id)
        if total:
            session.delete(total)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, total_id):
        return session.query(cls).get(total_id)

    def __repr__(self):
        return f"<Total id={self.id} month={self.month} total_amount={self.total_amount}>"

engine = create_engine('sqlite:////home/memoo/development/code/phase3/expense-tracker-cli/lib/app.db/app.db')
Session = sessionmaker(bind=engine)
session = Session()

