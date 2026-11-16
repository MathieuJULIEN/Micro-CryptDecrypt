import src.cryptage as cryptage
import src.decryptage as decryptage
import src.clear as clear
import src.error as error
import time
import sys


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
            print(error.err_choix_menu())
            time.sleep(3)
            clear.ClearCmd()
            continue
        


def StartProgram() :
    """
    Cette fonction est comme un Menu de lancement, on y choisi si l'on souhaite crypter un message,
    decrypter un message qui a était crypté par ce programme, ou meme pouvoir juste quitter.
    """
    clear.ClearCmd()
    while True:
        print(" Saisir le numéro correspondant à l'option que vous voulez utiliser : \n\n 1 - Cryptage \n 2 - Decryptage \n 0 - Quitter\n")
        ChoixOption=input("Option choisi : ")
        print("\n")
        if ChoixOption == "1" :
            clear.ClearCmd()
            print(cryptage.Encrypteur())
            ReturnMenu()
        elif ChoixOption == "2":
            clear.ClearCmd()
            print(decryptage.Decrypteur())
            ReturnMenu()
        elif ChoixOption == "0":
            clear.ClearCmd()
            if ConfirmExit() == True:
                break
            else :
                clear.ClearCmd()
                continue
        else :
            print(error.err_choix_menu())
            time.sleep(3)
            clear.ClearCmd()
            continue



def ReturnMenu() :
    while True :
        print("\n\nSouhaitez vous retourner au menu ou quitter ?\n\n 1 - Retour au menu \n 2 - Quitter l'application")
        saisi=input("\nOption sélectionné : ")
        if saisi == "1" :
            clear.ClearCmd()
            break
        elif saisi == "2" :
            clear.ClearCmd()
            if ConfirmExit() == True:
                sys.exit()
        else :
            print(error.err_choix_menu())
            time.sleep(3)
            clear.ClearCmd()
            continue