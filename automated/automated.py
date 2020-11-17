# Q1-3
def cesar(m, k):
    m = m.upper()
    msg = ""
    for i in range(0, len(m)):
        msg += chr(((ord(m[i]) - 65) + k)%26 + 65)
    return msg

# for i in range(0, 25):
#     print(str(i) + " : " + cesar("MILOBCOMZYVIDOMRKXQOBC", i))
#     # => CYBERSECPOLYTECHANGERS (i=16)

#Q4: a^-1 = 7
#Q5: pas de solutions car pas premiers entre eux
for i in range(0, 10):
    if((4*i)%9 == 1):
        print(i)

# Q6: Euclide étendu
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

def ChiffreAffine(m, a, b):
    m=m.upper()
    msg = ""
    for i in range(0, len(m)):
        msg += chr(((ord(m[i])-65) * a + b)%26 + 65)
    return msg

# Q7
def DechiffreAffine(msg, a, b):
    msg = msg.upper()
    m = ""
    inv = inv_mod(a, 26)
    for i in range(0, len(msg)):
        letter = ord(msg[i]) - 65
        m += chr(( (inv) * (letter - b )) % 26 + 65)
    return m

print(ChiffreAffine("ABCDEF", 11, 7)) # HSDOZK
print(DechiffreAffine("HSDOZK", 11, 7))

# Q8
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
    print(array_nb)
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
    array_nb = []
    for i in range(0, len(m), bloc_size):
        #if(i == 0 and int(m[i] + m[i+1]) == 0): continue
        message += m[i]
        for j in range(1, bloc_size):
            message += m[i+j]
    #print(message)
    ret = ""
    for i in range(0, len(message), 2):
        ret += chr(int(message[i] + message[i+1]) + 65)

    #print(ret)
    return ret

n, d, e = RSA(53, 11, 3)
print("n = " + str(n))
print("d = " + str(d))
res = encryptRSA("POLYTECHANGERS", n, e, 3)
print(res)
print(decryptRSA(res, d, n, 3))
# Avec 3, on a collisions des modulos (ici: 718 > 520). On a donc pas la garantie d'un message proprement chiffré / déchiffré.
# Il faut prendre une taille de bloc < log10(n) (donc augmenter n ou diminuer la taille de bloc. Augmenter n est mieux)
print("n = " + str(n))
#exit()
# Q13:
# Ex: k = 5
k = 5
print(EuclideEtendu(5, 583))
print("m   = 50")
mp = 50*pow(k, e) % n
print("m'  = " + str(mp))
mpp = pow(mp, d) % n
print("m'' = " + str(mpp))
(kinv, u, v) = EuclideEtendu(k, n)
kinv = u % n
print(kinv)
s = mpp * kinv % n
print("s = " + str(s))
print(pow(s, e)%n)
if(pow(s, e)%n == 50) :print("OK!")
else: print("Not OK!")
exit()
import copy
# Q14
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

print(Hash("BIENVENUEAPOLYTECHANGERS")) # YFFEGDKL
import random
import secrets
import string
alphabet = str.upper(string.ascii_letters)
def Prep():
    N = ''.join(secrets.choice(alphabet) for i in range(12))
    return N

class Cle(object):
    def __init__(self):
        self.N = Prep()
        self.hash = None
        self.voted = False
        return
    def SetHash(self, hash):
        self.hash = hash

class Commissaire(object):
    def __init__(self):
        self.lst = []
        self.distributed = 0
        for i in range(0, 20):
            self.lst.append(Cle())
        return

    def Distribute(self):
        val = self.lst[self.distributed]
        self.distributed += 1
        return val

    def ReceiveElecteurVal(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N:
                self.lst[i].hash = cle.hash
        return

    def Verify(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N and self.lst[i].hash == cle.hash:
                return True
        return False
    def HasVoted(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N and self.lst[i].hash == cle.hash:
                if self.lst[i].voted == True:
                    print("[Commissaire] Electeur a déjà voté !")
                    return False
                self.lst[i].voted = True
                return True
        return False

class Electeur(object):
    def __init__(self):
        return

    def ReceiveCode(self, commissaire, code):
        self.n1 = code
        self.n2 = Prep()
        self.vc = None
        self.n1.SetHash(Hash(self.n2))
        commissaire.ReceiveElecteurVal(self.n1)

    def Vote(self, anon, dec, admin, comm, vote):
        if admin.Contact(self.n1, comm):
            print("Code valid !")
            self.vote = vote + self.n2

            # Validate blind signature
            newm = []
            for i in range(0, len(self.vote)):
                val = (ord(self.vote[i]) - 65) % 26
                mp = val * pow(adm.dec.k, adm.dec.e) % adm.dec.n
                newm.append(mp)
            mpp = admin.BlindSign(newm)

            for i in range(0, len(mpp)):
                (kinv, u, v) = EuclideEtendu(adm.dec.k, adm.dec.n)
                kinv = u % adm.dec.n
                s = (mpp[i] * kinv) % adm.dec.n
                if(pow(s, adm.dec.e)%adm.dec.n != (ord(self.vote[i]) - 65)):
                    print("COULD NOT VALIDATE SIGNATURE (i=" + str(i) + ")")
                    return
            print("[Electeur] Signature validée !")

            self.vc = dec.Encrypt(self.vote)
            print(self.vc)
            anon.ReceiveVote(self.n1, self.vc, comm)
            return
        else:
            print("Code not valid!")
            return

class Administrator(object):
    def __init__(self):
        self.dec = Decompteur(53, 11, 27, 5)
        return
    def Contact(self, cle, commissaire):
        return commissaire.Verify(cle)
    def BlindSign(self, mp):
        array = []
        for i in range(0, len(mp)):
            array.append(pow(mp[i], self.dec.d) % self.dec.n)
        return array

class Decompteur(object):
    def __init__(self, p, q, e, k):
        self.p = p
        self.q = q
        self.e = e
        self.psy = (self.p - 1) * (self.q - 1)
        self.n, self.d, self.e = RSA(self.p, self.q, self.e)
        self.k = k
        a, b, c = EuclideEtendu(self.k, self.n)
        if(a != 1): print("Not correct k !!")
        else: print("Correct K")
        print(self.p, self.q, self.e, self.psy, self.n, self.d, self.k)

    def Encrypt(self, msg):
        val = encryptRSA(msg, self.n, self.e, 2)
        return val

    def Decompte(self, anon):
        for i in anon.votes:
            val = decryptRSA(i, self.d, self.n, 2)
            print(val)
        return

class Anonymiseur(object):
    def __init__(self):
        self.votes = []
        return

    def ReceiveVote(self, cle, vote, commissaire):
        if(not comm.HasVoted(cle)):
            print("[Anonymiseur] La vérification de la clé a échoué.")
            return
        self.votes.append(vote)

dec = Decompteur(53, 11, 27, 5)

comm = Commissaire()
el1 = Electeur()
el1.ReceiveCode(comm, comm.Distribute())

el2 = Electeur()
el2.ReceiveCode(comm, comm.Distribute())

el3 = Electeur()
el3.ReceiveCode(comm, comm.Distribute())

el4 = Electeur()
el4.ReceiveCode(comm, comm.Distribute())

anon = Anonymiseur()

adm = Administrator()
el1.Vote(anon, dec, adm, comm, "Z")
el2.Vote(anon, dec, adm, comm, "A")
el3.Vote(anon, dec, adm, comm, "B")
el4.Vote(anon, dec, adm, comm, "F")
print(el1.vote)
print(el2.vote)
print(el3.vote)
print(el4.vote)

dec.Decompte(anon)