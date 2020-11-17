from chiffrement_cesar import cesar
from dechiffrement_cesar import decodeCesar
from chiffrement_affine import chiffrementAffine
from dechiffrement_affine import dechiffreAffine
from chiffrement_rsa import RSA, encryptRSA
from dechiffrement_rsa import decryptRSA
from signature_aveugle import mPrime, mPrimePrime, sFunction, dechiffrementSignature

# ----------------------------- CÉSAR
print("\n CÉSAR \n")
print(cesar("CYBERSECPOLYTECHANGERS", ord("K")-65))
# TexteChiffre = input("\nVeuillez entrez la chaine de caractère chiffrée = ")
decodeCesar("MILOBCOMZYVIDOMRKXQOBC")

# ----------------------------- AFFINE
print("\n AFFINE \n")
a = 3
b = 10
textClair = "EXECUTE ORDER SIXTY SIX"
textChiffre = chiffrementAffine(textClair, a, b)
print("CHAINE CHIFFRÉE : " + textChiffre)
print(dechiffreAffine(textChiffre, a, b))

# ----------------------------- RSA
print("\n RSA \n")
n, d, e = RSA(53, 11, 3)
print(encryptRSA("POLYTECHANGERS", n, 3))
print(decryptRSA([1, 303, 481, 34, 453, 564, 1, 498, 127, 115], 347, 583, 3))

# ----------------------------- AVEUGLE
print("\n SIGNEMENT AVEUGLE \n")
p = 5
q = 11
e = 27
n, d, e = RSA(p, q, e)
k = 42 # Premier avec n

message = "M"
mP = mPrime(message, k, e, n) # Signer par Bob
mPP = mPrimePrime(mP, d, n) # Signé par Alice
s = sFunction(mPP, k, n) # Vérification par Bob

print("mP =", mP, " mPP =", mPP, " s =", s)
print("Déchiffrement : ", dechiffrementSignature(s, e, n))