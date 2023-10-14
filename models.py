import datetime
from .db import Base
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    UniqueConstraint,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.sql.expression import null, text
# from sqlalchemy.orm import relationship


class Country(Base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)


class State(Base):
    __tablename__ = "State"
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Country_id = Column(Integer, ForeignKey("Country.id"), nullable=False)


class Contacts(Base):
    __tablename__ = "Contacts"
    id = Column(Integer, primary_key=True)
    Firstname = Column(String, nullable=False)
    Lastname = Column(String, nullable=False)
    Email = Column(String, nullable=False, unique=True)
    MobileNo = Column(String, nullable=False)
    StateId = Column(Integer, ForeignKey("State.id"), nullable=False)
    # created_at = Column(
    #     TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    # )


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False, unique=True)
#     password = Column(String, nullable=False)
#     created_at = Column(
#         TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
#     )
