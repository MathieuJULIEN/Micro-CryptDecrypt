import src.cryptage as cryptage
import src.decryptage as decryptage
import src.clear as clear
import time


def ConfirmExit() :
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
            print("en cours de dev")
            break
        elif ChoixOption == "0":
            clear.ClearCmd()
            if ConfirmExit() == True:
                break
            else :
                clear.ClearCmd()
                continue