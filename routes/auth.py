from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import User
from schemas import UserCreate

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    # Validar si ya existe el email
    existe = db.query(User).filter(User.email == user.email).first()
    if existe:
        raise HTTPException(status_code=400, detail="El email ya está registrado")

    nuevo = User(
        name=user.name,
        email=user.email,
        password=user.password,
        phone=user.phone
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {
        "message": "Usuario registrado con éxito",
        "user_id": nuevo.id,
        "email": nuevo.email
    }
