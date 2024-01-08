import platform

from linuxcheck import linuxstart
from windowscheck import windowstart

os_info = platform.uname()

def printsys():
    print("操作系统类型：" + os_info[0])
    print("系统发行版：" + os_info[1])
    print("内核版本：" + os_info[2])

def checksysv():
    if os_info[0] == "Linux":
        linuxstart()
    elif os_info[0] == "Windows":
        windowstart()

