from helper import *
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

n, d, e = RSA(53, 11, 27)
print("n = " + str(n))
res = encryptRSA("POLYTECHANGERS", n, e, 2)
print(res)
print(decryptRSA(res, d, n, 2))
# Avec 3, on a collisions des modulos (ici: 718 > 520). On a donc pas la garantie d'un message proprement chiffré / déchiffré.
# Il faut prendre une taille de bloc < log10(n) (donc augmenter n ou diminuer la taille de bloc. Augmenter n est mieux)
print("n = " + str(n))

# Q13:
# Ex: k = 5
k = 5
print(EuclideEtendu(5, 583))
print("m   = 10")
mp = 10*pow(k, e) % n
print("m'  = " + str(mp))
mpp = pow(mp, d) % n
print("m'' = " + str(mpp))
(kinv, u, v) = EuclideEtendu(k, n)
kinv = u % n
s = mpp * kinv % n
print("s = " + str(s))
if(pow(s, e)%n == 10) :print("OK!")
else: print("Not OK!")


print(Hash("BIENVENUEAPOLYTECHANGERS")) # YFFEGDKL




from administrateur import *
from Decompteur import *
from electeur import *
from anonymiseur import *
from commissaire import *




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