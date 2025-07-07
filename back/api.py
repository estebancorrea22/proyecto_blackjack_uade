# blackjack_backend/main.py
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from registro_login import login_usuario, guardar_usuarios_json, modificar_saldo_usuario
from pydantic import BaseModel, EmailStr
from fastapi.responses import FileResponse, JSONResponse
import json
from typing import Optional, List
from datetime import datetime

from tirada_dados import tirar_dado, evaluar_mano, sumar_dados
from apuestas import doblar_apuesta_api, plantarse
from juego import determinar_ganador,chequear_total_crupier
from calcular_pago import calcular_pago
app = FastAPI()

# CORS setup so React can call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginRequest(BaseModel):
    correo: str
    contrasena: str 

class DoblarApuestaRequest(BaseModel):
    mano: List[int]
    saldo: int
    apuesta: int

class PlantarseRequest(BaseModel):
    mano: List[int]
    total: int
    apuesta: int

class DeterminarGanadorRequest(BaseModel):
    estado_jugador: str
    total_jugador: int
    estado_crupier: str
    total_crupier: int

class CalcularPagoRequest(BaseModel):
    resultado: str
    apuesta: int
    saldo: int


class Logro(BaseModel):
    id: int
    nombre: str
    descripcion: str
    recompensa: int

class Logros(BaseModel):
    logros_obtenidos: List[Logro]
    logros_disponibles: List[Logro]

class NuevoSaldoRequest(BaseModel):
    nuevo_saldo: int
    id_usuario: int


class UserToSaveRequest(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    contrasena: str
    saldo: int
    edad: int
    ultima_recarga: datetime
    ultimo_login: Optional[datetime] = None
    historial: List  # You can replace with List[YourHistorialModel] if you define it
    logros: Logros


@app.post("/start")
def start_game():
    return {"message": "Game started!"}

@app.post("/login")
def login(data: LoginRequest):
    print(f'Correo: {data.correo}, contrasena: {data.contrasena}')
    result = login_usuario(data.correo, data.contrasena, api=True)
    if(result == None):
        result = False
    
    print(f'Result: {result}')
    return result


@app.post("/startPlay")
def login():
    return 'result'

@app.get("/getUsers")
def getUsers():
    with open("usuarios.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # ← Converts JSON to Python list/dict
        response = JSONResponse(content=data)
        response.headers["Cache-Control"] = "no-store"
    return response

@app.post("/tirarDados")
def getUsers(tiradas: int = Body(...)):
    return tirar_dado(tiradas)

@app.post("/sumarDados")
def getUsers(mano: List[int]  = Body(...)):
    return sumar_dados(mano)

@app.post("/evaluarMano")
def getUsers(mano: List[int]  = Body(...)):
    return evaluar_mano(mano)

@app.post("/doblarApuesta")
def getUsers(data: DoblarApuestaRequest):
    return doblar_apuesta_api(data.mano, data.apuesta, data.saldo)

@app.post("/plantarse")
def getUsers(data: PlantarseRequest):
    return plantarse(data.total, data.mano, data.apuesta)

@app.post("/turnoCrupier")
def getUsers(mano: List[int]  = Body(...)):
 return chequear_total_crupier(mano)

@app.post("/calcularGanancias")
def getUsers(data:CalcularPagoRequest):
 return calcular_pago(data.resultado, data.apuesta, None, True, data.saldo)

@app.post("/nuevoSaldo")
def getUsers(data:NuevoSaldoRequest):
 return modificar_saldo_usuario(data.id_usuario, data.nuevo_saldo)

@app.post("/guardarDatos")
def getUsers(data:UserToSaveRequest):
 return guardar_usuarios_json(data)

@app.post("/determinarGanador")
def getUsers(data: DeterminarGanadorRequest):
    print(data)
    return determinar_ganador(data.estado_jugador, data.total_jugador, data.estado_crupier, data.total_crupier)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)