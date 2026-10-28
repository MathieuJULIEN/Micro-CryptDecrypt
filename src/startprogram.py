import src.cryptage as cryptage
import src.decryptage as decryptage
import src.clear as clear
import time


def ConfirmExit() :
    """
    Cette fonction s'occupe de la confirmation pour stop l'execution et quitter le programme.
    """
    while True :
        print("Êtes-vous sûre de vouloir quitter ? \n\n 1 - Quitter \n 2 - Annuler/Reprendre\n")
        abcdefg=input("Option choisi : ")
        if abcdefg=="1":
            clear.ClearCmd()
            return True
        elif abcdefg=="2":
            clear.ClearCmd()
            return False
        else :
            print("\nVous avez mal saisi, veuillez vérifier votre saisi.")
            time.sleep(1)
            clear.ClearCmd()
            continue
        


def StartProgram() :
    """
    Cette fonction est comme un Menu de lancement, on y choisi si l'on souhaite crypter un message,
    decrypter un message qui a était crypté par ce programme, ou meme pouvoir juste quitter.
    """
    clear.ClearCmd()
    while True:
        print("\n Saisir le numéro correspondant à l'option que vous voulez utiliser : \n\n 1 - Cryptage \n 2 - Decryptage \n 0 - Quitter\n")
        ChoixOption=input("Option choisi : ")
        print("\n")
        if ChoixOption == "1" :
            clear.ClearCmd()
            print(cryptage.Encrypteur())
            break
        elif ChoixOption == "2":
            clear.ClearCmd()
            print(decryptage.Decrypteur())
            break
        elif ChoixOption == "0":
            clear.ClearCmd()
            if ConfirmExit() == True:
                break
            else :
                clear.ClearCmd()
                continue
        else :
            print("\nVous avez mal saisi, veuillez vérifier votre saisi.")
            time.sleep(1)
            clear.ClearCmd()
            continue