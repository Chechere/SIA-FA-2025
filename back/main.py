from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os, io
from urllib.request import urlopen

from ipgetter import *
from qrgenerator import *
from race import RaceController

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload


local_ip = get_local_ip()

urlBase = "http://" + local_ip + ":8000/"

print("\n URL base de la pagina web: ", 
        "\033[1m" + urlBase + "\033[0m\n")

generateqr(urlBase).print_ascii()

urlDesarrollador = urlBase + "/desarrollador"

print("\nEres desarrollador? Entra aqui:",
        "\033[1m" + urlDesarrollador + "\033[0m\n")

raceController = RaceController()

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
    if(raceController.checkRaceId(raceId)):
        return Response(status_code=200)
    else:
        #return Response(status_code=404)
        return Response(status_code=200)

def checkUserName(user: str) -> bool:
    if(user == None or user == "" or raceController.playerRegistered(user)):
        return False

    return True

@api_router.post("/registerUser")
def registerUser(user: str):
    if(checkUserName(user)):
        raceController.registerPlayer(user)
        return Response(status_code=201)

    return Response(status_code=403)

@api_router.post("/newGame")
def createNewGame():
    raceController.createNewRace()
    pass

@api_router.get("/getRaceQR")
def raceQrCode():
    urlRace = urlBase + "/race?raceId=" + str(raceController.getRaceId())
    qrBytes = createImage(generateqr(urlRace), "../front/resources/IEEE_Logo_Formula.png")
    #qrBytes = io.BytesIO()

    #generateqr(urlRace).make_image( embeded_image_path="../front/IEEE_Logo_Formula.png").save(qrBytes, format="PNG")

    return Response(content=qrBytes.getvalue(), media_type="image/png")


app.include_router(api_router, prefix="/api")
app.mount("/", StaticFiles(directory="../front", html=True), name="front")

