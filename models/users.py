from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from bd import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    phone = Column(Text)
    role = Column(Text, nullable=False, default="user")
    created_at = Column(TIMESTAMP)
