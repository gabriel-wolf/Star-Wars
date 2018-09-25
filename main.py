from settings import Settings
from pygame import mixer
from rooms import Rooms
import time
from os import system, name
import sys
import ctypes
from ctypes import POINTER, WinDLL, Structure, sizeof, byref
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE

def rungame():

    skiptitle = False
    if(skiptitle == True):
        Rooms()
    else:
        None

    _ = system('cls')

    time.sleep(1)

    print(
    "\n\n\n\n\n\n\n\n\n\n\n"
    "                                                    A long time ago\n"
    "                                                In a galaxy far, far away...\n"
    )


    time.sleep(4.5)

    _ = system('cls')

    # play music
    mixer.init()
    mixer.music.load('ThemeSong.mp3')
    mixer.music.play()


    print(
    "\n\n\n\n"
    "                                        ________________.  ___     .______\n"
    "                                       /                | /   \    |   _  \\\n"
    "                                      |   (-----|  |----`/  ^  \   |  |_)  |\n"
    "                                       \   \    |  |    /  /_\  \  |      /\n"
    "                                  .-----)   |   |  |   /  _____  \ |  |\  \-------.\n"
    "                                  |________/    |__|  /__/     \__\| _| `.________|\n"
    "                                  ____    __    ____  ___     .______    ________.\n"
    "                                  \   \  /  \  /   / /   \    |   _  \  /        |\n"
    "                                   \   \/    \/   / /  ^  \   |  |_)  ||   (-----`\n"
    "                                    \            / /  /_\  \  |      /  \   \\\n"
    "                                     \    /\    / /  _____  \ |  |\  \---)   |\n"
    "                                      \__/  \__/ /__/     \__\|__| `._______/\n"
    "\n"
    "                                   ------------------------------------------------"
    "                                                                                   Created By: Gabriel Wolf"
    "\n\n"
    )


    time.sleep(5)


    print("\n\n"
    "                                                Press ENTER to Start...")
    input()
    # stop music
    mixer.music.fadeout(3000)
    time.sleep(3)

    _ = system('cls')


    time.sleep(0.5)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    print("                                         Leia races home aboard her")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    print("                                         Leia races home aboard her")
    print("                                         starship, custodian of the")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    print("                                         Leia races home aboard her")
    print("                                         starship, custodian of the")
    print("                                         stolen plans that can save")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    print("                                         Leia races home aboard her")
    print("                                         starship, custodian of the")
    print("                                         stolen plans that can save")
    print(                                         "her people and restore")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n\n")
    print("                                         It is a period of civil war.")
    print("                                         Rebel spaceships, striking")
    print("                                         Rebel spaceships, striking")
    print("                                         from a hidden base, have won")
    print("                                         their first victory against")
    print("                                         the evil Galactic Empire.")
    print("                                         ")
    print("                                         During the battle, Rebel")
    print("                                         spies managed to steal secret")
    print("                                         plans to the Empire's")
    print("                                         ultimate weapon, the DEATH")
    print("                                         STAR, an armored space")
    print("                                         station with enough power to")
    print("                                         destroy an entire planet.")
    print("                                         ")
    print("                                         Pursued by the Empire's")
    print("                                         sinister agents, Princess")
    print("                                         Leia races home aboard her")
    print("                                         starship, custodian of the")
    print("                                         stolen plans that can save")
    print("                                         her people and restore")
    print("                                         reedom to the galaxy.....")
    time.sleep(0.5)
    _ = system('cls')
    print("\n\n\n\n\n\n\n")






    time.sleep(1.75)

    Rooms()



LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    _fields_ = [("X", SHORT), ("Y", SHORT)]

class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [("cbSize", ULONG),
                ("nFont", DWORD),
                ("dwFontSize", COORD),
                ("FontFamily", UINT),
                ("FontWeight", UINT),
                ("FaceName", WCHAR * LF_FACESIZE)]



font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 11
font.dwFontSize.X = 5
font.dwFontSize.Y = 12
font.FontFamily = 54
font.FontWeight = 800
font.FaceName = "Perfect DOS VGA 437 Win"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))


rungame()
