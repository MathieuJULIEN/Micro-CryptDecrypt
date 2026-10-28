def Decrypteur():
    messagecrypte=input("Saisir votre message Crypté : ")
    sommepourcle=0
    texteuncrypt=""
    caractere="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,;/!%éàèêîôöïë()[]=+-@&1234567890*$_<>|~'.?"
    caractereswap="Hride4xSB UyVg._IöTZbvp@Fé5D78nP~,=jJ6RNo!lè'm[K?tX+O*$|qGWaêzQMôEYsîL-ï%/<ë;3C2(9wA>1)]&àcukh0f"
    for i in range(0,5):
        sommepourcle+=int(messagecrypte[i])
    rouedecesar=caractereswap[sommepourcle:]+caractereswap[:sommepourcle]
    for y in range(6,len(messagecrypte)):
        for z in range(96):
            if messagecrypte[y]==rouedecesar[z]:
                texteuncrypt+=caractere[z]
                break
            else:
                if z==95:
                    texteuncrypt+=messagecrypte[y]
    return texteuncrypt