# blackjack_backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from registro_login import login_usuario
from pydantic import BaseModel

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


@app.post("/start")
def start_game():
    return {"message": "Game started!"}

@app.post("/login")
def login(data: LoginRequest):
    result = login_usuario(data.correo, data.contrasena, api=True)
    print(f'Result: {result}')
    return result


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)