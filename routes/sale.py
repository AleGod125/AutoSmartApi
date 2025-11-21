from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.modelSale import Sale
from models.model_Vehicule import Vehicle
from models.models_Auht import User
from Schemas.schemas_Sale import SaleCreate, SaleOut
import random

router = APIRouter(prefix="/sales", tags=["Sales"])

METODOS = [
    "Transferencia Bancaria",
    "Financiamiento",
    "Tarjeta de Crédito"
]

# CREAR VENTA
@router.post("/create", response_model=SaleOut)
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):

    vehicle = db.query(Vehicle).filter(Vehicle.id == data.vehicle_id).first()
    if not vehicle:
        raise HTTPException(404, "Vehículo no encontrado")

    buyer = db.query(User).filter(User.id == data.buyer_id).first()
    if not buyer:
        raise HTTPException(404, "Usuario no encontrado")

    last = db.query(Sale).order_by(Sale.id.desc()).first()
    next_id = 1 if not last else last.id + 1
    invoice_number = f"INV-2024-{str(next_id).zfill(3)}"

    sale = Sale(
        invoice_number=invoice_number,
        vehicle_id=data.vehicle_id,
        buyer_id=data.buyer_id,
        amount=data.amount,
        payment_method=random.choice(METODOS)
    )

    db.add(sale)
    db.commit()
    db.refresh(sale)
    return sale


# LISTAR VENTAS
@router.get("/all", response_model=list[SaleOut])
def get_sales(db: Session = Depends(get_db)):
    return db.query(Sale).order_by(Sale.date.desc()).all()
