# services/user_service.py
from repositories.user import get_by_email, create_user
from utils.security import hash_password, verify_password

def signup_service(db, data):
    # verificar si existe
    if get_by_email(db, data.email):
        raise Exception("El correo ya está registrado 🤨")

    user_data = data.dict()
    user_data["password"] = hash_password(data.password)

    return create_user(db, user_data)

def login_service(db, email: str, password: str):
    user = get_by_email(db, email)
    if not user:
        raise Exception("Correo incorrecto 😒")

    if not verify_password(password, user.password):
        raise Exception("Contraseña incorrecta 😑")

    return user  # Aquí luego puedes generar un JWT
