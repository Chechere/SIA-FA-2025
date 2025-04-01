from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import qrcode

import os
from enum import Enum
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM, setdefaulttimeout, error
from urllib.request import urlopen

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload

def get_local_ip():
    google_dns = "8.8.8.8"
    port = 80

    try:
        connection = socket(AF_INET, SOCK_DGRAM)
        connection.connect((google_dns, port))
        local_ip_address = connection.getsockname()[0]
        return local_ip_address
    except Exception as e:
        print(e)
        return None
    finally:
        connection.close()


local_ip = get_local_ip()

urlBase = "http://" + local_ip + ":8000/"

print("\n URL base de la pagina web: ", 
        "\033[1m" + urlBase + "\033[0m\n")

qrBase = qrcode.QRCode()
qrBase.add_data(urlBase)
qrBase.make()
qrBase.print_ascii()

urlDesarrollador = urlBase + "/desarrollador"

print("\nEres desarrollador? Entra aqui:",
        "\033[1m" + urlDesarrollador + "\033[0m\n")

qrDes = qrcode.QRCode()
qrDes.add_data(urlDesarrollador)
qrDes.make()
qrDes.print_ascii()

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

