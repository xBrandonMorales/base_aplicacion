from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configura la conexión a MongoDB Atlas
MONGO_URL = "mongodb+srv://Brandon:12345@proyectfut.t6xvu52.mongodb.net/?retryWrites=true&w=majority&appName=ProyectFut"
client = AsyncIOMotorClient(MONGO_URL)
db = client.proyecto  # Reemplaza "test_database" con el nombre de tu base de datos

class Equipo(BaseModel):
    nombre: str
    capitan: str
    correo_capitan: str
    entrenador: str

@app.get("/equipos/", response_model=List[Equipo], summary="Obtener todos los equipos", description="Devuelve una lista de todos los equipos en la base de datos.")
async def get_equipos():
    equipos = await db.equipos.find().to_list(None)
    return equipos

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
