from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String, Double, ForeignKey, Table, Enum
from sqlalchemy.orm import relationship, backref, declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, name="id", primary_key=True, index=True)
    name = Column(String, name="name", unique=True)
    subcategories = relationship('Subcategory', backref='category', lazy=True)


class Subcategory(Base):
    __tablename__ = "subcategory"
    id = Column(Integer, name="id", primary_key=True, index=True)
    name = Column(String, name="name", unique=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    subcategories = relationship('Product', backref='subcategory', lazy=True)


product_character_link = Table('product_character_link',
                               Base.metadata,
                               Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
                               Column('characteristic_id', Integer, ForeignKey('characteristic.id'), primary_key=True)
                               )


class Status(PyEnum):
    PENDING = "pending"
    ACTIVE = "active"
    BANED = "baned"
    SOLD = "sold"


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, name="id", primary_key=True, index=True)
    vendor_code = Column(String, name="vendor_code", unique=True)
    name = Column(String, name="name")
    price = Column(Double, name="price")
    quantity = Column(Integer, name="quantity")
    status = Column(Enum(Status), name="status", default=Status.ACTIVE)
    subcategory_id = Column(Integer, ForeignKey("subcategory.id"), nullable=False)
    characteristics = relationship('Characteristic', secondary=product_character_link, lazy='subquery',
                                   backref=backref('product', lazy=True))


class Characteristic(Base):
    __tablename__ = "characteristic"
    id = Column(Integer, name="id", primary_key=True, index=True)
    name = Column(String, name="name", unique=True)
