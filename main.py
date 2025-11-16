from fastapi import FastAPI
from routes.auth import router as auth_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hola mundo"}

app.include_router(auth_router)
