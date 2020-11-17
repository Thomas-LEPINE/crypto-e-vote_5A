from chiffrement_cesar import cesar

def decodeCesar(m) :
    print("\n-> Combinaisons possibles :\n")
    for i in range(1, 26):
        print(str(i) + " : " + cesar(m, i))