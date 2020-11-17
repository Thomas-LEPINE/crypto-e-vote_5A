import copy

'''
Hashage TTH()
input = msg : string (Chaine claire)
output = hash : string (Chaine hachée)
'''
def Hash(msg):
    NB_COLONNES = 4
    BLOCKSIZE = NB_COLONNES**2

    msg = msg.upper() # On met en majuscule le message
    array = []
    IV = [0] * NB_COLONNES
    for i in range(0, len(msg), BLOCKSIZE) : # Création de la OU des matrice(s) comportants les caracètres (limité à 16s)
        array.append(msg[i:i+BLOCKSIZE:1].ljust(BLOCKSIZE, 'A'))
    
    hash = ""
    val = 0
    for message in array:
        array_1 = []
        for i in range(0, NB_COLONNES) :
            val = ((ord(message[i]) + ord(message[i+4]) + ord(message[i+8]) + ord(message[i+12]) - NB_COLONNES*65)+IV[i])%26
            array_1.append(val)
        
        # Création de la deuxième "matrice" ou l'on effectue des permutations
        newmsg = ""
        for i in range(0, BLOCKSIZE, NB_COLONNES):
            if i == 0: val = message[i+1] + message[i+2] + message[i+3] + message[i]
            if i == 4: val = message[i+2] + message[i+3] + message[i] + message[i+1]
            if i == 8: val = message[i+3] + message[i] + message[i+1] + message[i+2]
            if i == 12: val = message[i+3] + message[i+2] + message[i+1] + message[i]
            newmsg += val
        
        # Addition des colonnes de la 2eme matrice
        array_2 = []
        for i in range(0, NB_COLONNES) :
            val = (ord(newmsg[i]) + ord(newmsg[i+4]) + ord(newmsg[i+8]) + ord(newmsg[i+12]) - NB_COLONNES*65)%26
            array_2.append(val)

        newIV = []
        # Addition des 2 matrices :
        for i in range(0, NB_COLONNES) :
            val = (array_1[i]+array_2[i])%26
            newIV.append(val)
            hash += chr(newIV[i] % 26 + 65)
            
        IV = copy.deepcopy(newIV) # Définition du nouveau IV par copy
    return hash

print(Hash("BIENVENUEAPOLYTECHANGERS"))