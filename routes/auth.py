from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models.models_Auht import User
from Schemas.schemas_Auht import UserCreate, UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.email == data.email).first()

        if not user:
            raise HTTPException(status_code=404, detail="El usuario no existe")

        if user.password != data.password:
            raise HTTPException(status_code=401, detail="Contraseña incorrecta")

        return {
            "message": "Inicio de sesión exitoso",
            "user_id": user.id,
            "role": user.role,
            "name": user.name
        }

    except Exception as e:
        print("ERROR LOGIN:", e)
        raise HTTPException(status_code=500, detail="Error interno en login")

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
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

