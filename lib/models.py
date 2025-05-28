from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)

engine = create_engine('sqlite:////home/memoo/development/code/phase3/expense-tracker-cli/lib/app.db/app.db')
Session = sessionmaker(bind=engine)
session = Session()
