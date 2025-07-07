# blackjack_backend/main.py
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from registro_login import login_usuario
from pydantic import BaseModel
from fastapi.responses import FileResponse, JSONResponse
import json
from typing import List
from tirada_dados import tirar_dado
from juego import evaluar_mano, doblar_apuesta

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
    apuesta_actual: int

@app.post("/start")
def start_game():
    return {"message": "Game started!"}

@app.post("/login")
def login(data: LoginRequest):
    result = login_usuario(data.correo, data.contrasena, api=True)
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

@app.post("/evaluarMano")
def getUsers(mano: List[int]  = Body(...)):
    return evaluar_mano(mano)

@app.post("/doblarApuesta")
def getUsers(data: DoblarApuestaRequest):
    return doblar_apuesta(data.mano, data.apuesta_actual, data.saldo)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)