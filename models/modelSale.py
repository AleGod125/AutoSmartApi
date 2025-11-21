from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, nullable=False)

    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    amount = Column(Numeric(12,2), nullable=False)
    payment_method = Column(String, nullable=False)

    date = Column(DateTime, default=datetime.utcnow)

    vehicle = relationship("Vehicle")
    buyer = relationship("User")
