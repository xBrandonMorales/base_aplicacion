from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configura la conexión a MongoDB Atlas
MONGO_URL = "mongodb+srv://Brandon:12345@proyectfut.t6xvu52.mongodb.net/?retryWrites=true&w=majority&appName=ProyectFut"
client = AsyncIOMotorClient(MONGO_URL)
db = client.proyecto  # Reemplaza "test_database" con el nombre de tu base de datos

class Equipo(BaseModel):
    _id: str
    id_equipo: int
    liga: str
    puntos: int
    nombre: str
    capitan: str
    correo: str
    entrenador: str
    numero_telefono: str

class Jugador(BaseModel):
    id: int
    nombre: str
    curp: str
    puntos: int
    asistencias: int
    remates: int
    goles: int
    tarjetas_amarillas: int
    tarjetas_rojas: int
    categoria: int

# Configuración de CORS para permitir acceso desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/jugadores/", response_model=List[Jugador], summary="Obtener todos los jugadores", description="Devuelve una lista de todos los jugadores en la base de datos.")
async def get_jugadores():
    jugadores = await db.jugadores.find().to_list(None)
    return jugadores

@app.get("/equipos/", response_model=List[Equipo], summary="Obtener todos los equipos", description="Devuelve una lista de todos los equipos en la base de datos.")
async def get_equipos():
    equipos = await db.equipos.find().to_list(None)
    return equipos

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
