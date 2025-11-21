from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    vehicle_id: int
    buyer_id: int
    amount: float

class SaleCreate(SaleBase):
    pass

class SaleOut(BaseModel):
    id: int
    invoice_number: str
    vehicle_id: int
    buyer_id: int
    amount: float
    payment_method: str
    date: datetime

    class Config:
        from_attributes = True
