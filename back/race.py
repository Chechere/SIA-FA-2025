from enum import Enum, auto
import random

class RaceStatus(Enum):
    PREPARACION = auto()
    CURSO = auto()
    FINALIZADA = auto()

class RaceController():
    def __init__(self):
        self.status: RaceStatus = RaceStatus.FINALIZADA
        self.players: [str] = []
        self.raceId: int = 12345678

    def createNewRace(self) -> bool:
        if(self.status == RaceStatus.CURSO): return False 
        self.players = []
        self.raceId = random.randint(10000000, 99999999)
        self.status = RaceStatus.PREPARACION
        return True

    def getRaceId(self) -> int:
        return self.raceId

    def checkRaceId(self, raceId) -> bool:
        if(self.status == RaceStatus.FINALIZADA):
            return False
        if(self.raceId != raceId):
            return False

        return True

    def playerRegistered(self, player) -> bool:
        return player in self.players

    def registerPlayer(self, player):
        self.players.append(player)

