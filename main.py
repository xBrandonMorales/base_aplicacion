from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configura la conexión a MongoDB Atlas
MONGO_URL = "mongodb+srv://brandon:12345@cluster0.w8r4vcx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URL)
db = client.test_database  # Reemplaza "test_database" con el nombre de tu base de datos

class Equipo(BaseModel):
    identificacion: str
    nombre: str
    capitan: str
    correo_capitan: str
    entrenador: str

# Obtener todos los equipos
@app.get("/equipos/", response_model=List[Equipo], summary="Obtener todos los equipos", description="Devuelve una lista de todos los equipos en la base de datos.")
async def get_equipos():
    equipos = db.equipos.find({})
    return [equipo for equipo in equipos]

# Obtener un equipo por su identificación
@app.get("/equipos/{identificacion}", response_model=Equipo, summary="Obtener un equipo por su identificación", description="Devuelve los detalles de un equipo específico identificado por su identificación única.")
async def get_equipo(identificacion: str):
    equipo = db.equipos.find_one({"identificacion": identificacion})
    if equipo is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo
