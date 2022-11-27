from xmlrpc.client import Boolean
from sqlalchemy import create_engine, MetaData, Table, Column, BigInteger, Date,  Integer, String, Boolean
from sqlalchemy.orm import declarative_base, registry, sessionmaker
engine = create_engine("postgresql://user:password@hostname/database_name")


# declarative base class
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    first_name = Column(String, nullable = True)
    second_name = Column(String, nullable = True)
    tg_name = Column(String, nullable = True)
    role = Column(String, nullable = True)
    in_editing = Column(String, nullable = True)
    is_banned = Column(Boolean, nullable = True)
    news_in_process = Column(String, nullable = True)


    def __init__(self, id, first_name, second_name, tg_name, role, in_editing, is_banned):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name
        self.tg_name = tg_name
        self.role = role
        self.in_editing = in_editing
        self.is_banned = is_banned

    def __repr__(self):
        return self.tg_name