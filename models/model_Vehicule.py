from sqlalchemy import Column, Integer, String, Float, Numeric, Text, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from db import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine_size = Column(Float, nullable=False)
    fuel = Column(String, nullable=False)
    transmission = Column(String, nullable=False)
    km = Column(Integer, nullable=False)
    condition = Column(String, nullable=False)
    price = Column(Numeric(12, 2), nullable=False)
    img = Column(Text, nullable=False) 
    propietario_id = Column(Integer, ForeignKey("users.id"))
    descripcion = Column(Text)
    approved = Column(Boolean, nullable=False, default=False)

    images = relationship("VehicleImage", back_populates="vehicle", cascade="all, delete")
    propietario = relationship("User", back_populates="vehiculos")





class VehicleImage(Base):
    __tablename__ = "vehicle_images"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id", ondelete="CASCADE"))
    url = Column(Text, nullable=False)

    vehicle = relationship("Vehicle", back_populates="images")