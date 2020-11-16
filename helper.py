import secrets
import string
import copy

ALPHABET = str.upper(string.ascii_letters) # ALPHABET # Chaine de caractère avec toutes les lettre de l'alpabet

def InputArray(str):
    array = input(str)
    array = array.replace("[", "")
    array = array.replace(" ", "")
    array = array.replace("]", "")
    print(array)
    array_sep = array.split(",")
    res = []
    for i in range(0, len(array_sep)):
        res.append(int(array_sep[i]))
    return res

def EuclideEtendu(a, b):
    (r, u, v, rp, up, vp) = (a, 1, 0, b, 0, 1)
    q = 0
    while (rp != 0):
        q = (r // rp)
        (r, u, v, rp, up, vp) = (rp, up, vp, r-q*rp, u-q*up, v-q*vp)

    return (r, u, v)

def inv_mod(n, mod):
    x, u, v = EuclideEtendu(n, mod)
    return u % mod

def RSA(p, q, e):
    n = p * q
    psy = (p-1) * (q-1)
    # x, u, v = EuclideEtendu(e, psy)
    # d = u % psy
    d = inv_mod(e, psy)
    return (n, d, e)

def encryptRSA(msg, n, e, bloc_size):
    msg = msg.upper()
    m = ""
    for i in range(0, len(msg)):
        rang = ord(msg[i]) - 65
        m += str(rang).zfill(2)
    array_nb = []
    for i in range(len(m)-1, -1, -bloc_size):
        nb = m[i]
        for j in range(1, bloc_size):
            if(i - j >= 0):  nb += m[i-j]
        array_nb.append(nb[::-1])
    array_nb = array_nb[::-1]
    array_encrypted = []
    for i in range(0, len(array_nb)):
        array_encrypted.append(pow(int(array_nb[i]), e) % n)
    return array_encrypted

def decryptRSA(msg, d, n, bloc_size):
    m = ""
    for i in range(0, len(msg)):
        val = msg[i]
        uncrypted = pow(val, d) % n
        m += str(uncrypted).zfill(bloc_size)
    message=""
    for i in range(0, len(m), bloc_size):
        #if(i == 0 and int(m[i] + m[i+1]) == 0): continue
        val = int(m[i] + m[i+1])
        message += (chr(val + 65))
    return message

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


'''
Génère le N1
'''
def Prep():
    N = ''.join(secrets.choice(ALPHABET) for i in range(12))
    return N