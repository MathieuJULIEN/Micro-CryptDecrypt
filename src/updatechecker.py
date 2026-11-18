import requests

def UpdateCheker() :
    """
    Cette fonction s'occupe de vérifier si le logiciel est à jour ou non.
    Elle emploie l'API de Github pour comparé la version que vous possèdez actuellement avec la version de la dernière Release.
    """
    #Version ACTU
    VErsionNow = "v1.0"

    r = requests.get('https://api.github.com/repos/MathieuJULIEN/Micro-CryptDecrypt/releases/latest')
    data = r.json()
    LatestVersion = data['tag_name']
    if VErsionNow==LatestVersion:
        return False
    else :
        return True
