def ReadTxt():
    """
    Permet de récupérer le contenu d'un fichier txt
    """
    namefile = input("Saisir le Nom de votre fichier .txt : ")
    veriftxt=""
    if len(namefile)>4:
        for i in range(4):
            j=4-i
            veriftxt+=namefile[len(namefile)-j]
    if veriftxt!=".txt":
        namefile+=".txt"
    runfile = "txt/"+namefile
    file = open(runfile,"r",encoding="utf-8")
    return file.read()