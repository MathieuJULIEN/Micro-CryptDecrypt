import os

def ClearCmd():
    """
    Cette fonction s'occupe uniquement de clear le Terminal afin d'avoir un interface plus propre sans tout l'historique juste au dessus.
    """
    os.system('cls' if os.name == 'nt' else 'clear')