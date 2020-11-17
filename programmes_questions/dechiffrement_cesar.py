def cesar(m, k):
    m = m.upper()
    msg = ""
    for cac in m :
        if(cac == " ") :
            msg += cac
        else :
            msg += chr(((ord(cac) - 65) + k)%26 + 65)
    return msg

TexteChiffre = input("\nVeuillez entrez la chaine de caractère chiffrée = ")

print("\n-> Combinaisons possibles :\n")
for i in range(1, 26):
    print(str(i) + " : " + cesar(TexteChiffre, i))

# MILOBCOMZYVIDOMRKXQOBC = CYBERSECPOLYTECHANGERS (Clé = K (16))