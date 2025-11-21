from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.orm import relationship
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String)
    role = Column(String, nullable=False, server_default="user")
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))

    vehiculos = relationship("Vehicle", back_populates="propietario")

