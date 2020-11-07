from os import system
import platform
sistema = platform.system()
# On efface le terminal avant de commencer la partie
def clear():
    if sistema == "Darwin" or sistema == "Linux":  # Verification du Operating system sur lequelle on travaille
        efface = "clear"  # Si MACINTOSH ou LINUX : clear
        system(efface)
    else:
        efface = "cls"
        system(efface)
