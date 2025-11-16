# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bd import get_db
from schemas.users import UserCreate, UserLogin
from services.users_service import signup_service, login_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return signup_service(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    try:
        user = login_service(db, data.email, data.password)
        return {"message": "Login exitoso", "user_id": user.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
