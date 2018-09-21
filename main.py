from settings import Settings
from rooms import Rooms

def rungame():
    settings = Settings()
    rooms = Rooms()

    while True:
        if(myroom == "Armory"):
            rooms.Armory()

myroom = "Armory"
rungame()
