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
