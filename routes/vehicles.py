from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.model_Vehicule import Vehicle, VehicleImage  
from Schemas.vehiculeSchemas import VehicleCreate, VehicleOut
from typing import List


router = APIRouter(prefix="/vehicles", tags=["Vehicles"])


@router.post("/saveVehicule", response_model=VehicleOut)
def create_vehicle(data: VehicleCreate, db: Session = Depends(get_db)):

    # Si no trae imágenes es un error
    if len(data.images) == 0:
        raise HTTPException(status_code=400, detail="Debes enviar al menos una imagen")

    # La primera imagen siempre será la principal
    imagen_principal = data.images[0].url

    # Crear vehículo con la imagen principal
    new_vehicle = Vehicle(
        type=data.type,
        brand=data.brand,
        model=data.model,
        year=data.year,
        engine_size=data.engine_size,
        fuel=data.fuel,
        transmission=data.transmission,
        km=data.km,
        condition=data.condition,
        price=data.price,
        img=imagen_principal,
        propietario_id=data.propietario_id,
        descripcion=data.descripcion,
        approved=False 
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    # Guardar otras imágenes (si existen)
    if len(data.images) > 1:
        for img in data.images[1:]:  # desde la segunda en adelante
            new_img = VehicleImage(vehicle_id=new_vehicle.id, url=img.url)
            db.add(new_img)

        db.commit()

    db.refresh(new_vehicle)
    return new_vehicle

@router.get("/pending", response_model=List[VehicleOut])
def get_pending_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).filter(Vehicle.approved == False).all()
    return vehicles

@router.get("/inventario", response_model=List[VehicleOut])
def get_pending_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(Vehicle).filter(Vehicle.approved == True).all()
    return vehicles

@router.put("/approve/{vehicle_id}")
def approve_vehicle(vehicle_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    vehicle.approved = True
    db.commit()
    db.refresh(vehicle)

    return {"message": "Vehículo aprobado exitosamente"}
