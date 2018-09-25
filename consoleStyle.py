import ctypes
import sys
from ctypes import POINTER, WinDLL, Structure, sizeof, byref
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE

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
font.dwFontSize.X = 4
font.dwFontSize.Y = 11
font.FontFamily = 54
font.FontWeight = 800
font.FaceName = "Perfect DOS VGA 437 Win"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        handle, ctypes.c_long(False), ctypes.pointer(font))
