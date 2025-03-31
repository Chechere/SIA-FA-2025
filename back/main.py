from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
from enum import Enum

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

print("\nEres desarrollador? Entra aqui:",
        "\033[1mhttp://0.0.0.0:8000/desarrollador\033[0m\n")


actualRaceId: int = 12345678
usersPlaying: list[str] = []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter()

@api_router.get("/checkRaceId")
def checkRaceId(raceId: int):
    if(raceId == actualRaceId):
        return Response(status_code=200)
    else:
        #return Response(status_code=404)
        return Response(status_code=200)

#@api_router.get("/checkUserName")
def checkUserName(user: str) -> bool:
    if(user == None or user == "" or user in usersPlaying):
        return False

    return True

@api_router.post("/registerUser")
def registerUser(user: str):
    if(checkUserName(user)):
        usersPlaying.append(user)
        return Response(status_code=201)

    return Response(status_code=403)


@api_router.get("") #localhost:8000/api
def read_message1():
    return { "message": "Hola desde al api" }

@api_router.get("/message") #localhost:8000/api/message
def read_message2():
    return {"message": "Hola desde el backend!"}

app.include_router(api_router, prefix="/api")
app.mount("/", StaticFiles(directory="../front", html=True), name="front")

