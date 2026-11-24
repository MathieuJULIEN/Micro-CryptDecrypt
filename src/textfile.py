import time
import src.clear as clear

def ReadTxt():
    """
    Permet de récupérer le contenu d'un fichier txt
    """
    while True :
        namefile = input("Saisir le Nom de votre fichier .txt : ")
        veriftxt=""
        if len(namefile)>4:
            veriftxt+=namefile[len(namefile)-4:]
        if veriftxt!=".txt":
            namefile+=".txt"
        runfile = "txt/"+namefile
        try:
            file = open(runfile,"r",encoding="utf-8")
        except FileNotFoundError:
            clear.ClearCmd()
            print("\nNom de Fichier Non valide, veuillez vérifier votre saisi\n")
            time.sleep(2)
            continue
        break
    return file.read()