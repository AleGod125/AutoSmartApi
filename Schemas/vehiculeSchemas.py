from pydantic import BaseModel
from typing import Optional, List
from decimal import Decimal

class VehicleImageBase(BaseModel):
    url: str

class VehicleImageCreate(VehicleImageBase):
    pass

class VehicleImageOut(VehicleImageBase):
    id: int

    class Config:
        orm_mode = True  # <- CORREGIDO

class VehicleBase(BaseModel):
    type: str
    brand: str
    model: str
    year: int
    engine_size: float
    fuel: str
    transmission: str
    km: int
    condition: str
    price: Decimal
    img: Optional[str] = None   
    propietario_id: int
    descripcion: Optional[str] = None
    approved: Optional[bool] = None


class VehicleCreate(VehicleBase):
    images: List[VehicleImageCreate]

class UserOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class VehicleOut(VehicleBase):
    id: int
    images: List[VehicleImageOut]
    propietario: Optional[UserOut]  

    class Config:
        orm_mode = True

