
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

class Product(Base):
    _tablename_ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)

    transactions = relationship("Transaction", back_populates="product")

class Transaction(Base):
    _tablename_ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    product = relationship("Product", back_populates="transactions")

class Supplier(Base):
    _tablename_ = 'suppliers'

    supplier_id = Column(Integer, primary_key=True)
    supplier_name = Column(String, nullable=False)