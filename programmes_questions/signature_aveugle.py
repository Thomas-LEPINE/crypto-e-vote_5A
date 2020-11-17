import string
ALPHABET = str.upper(string.ascii_letters)

def rangLettre(lettre):
    rang = ALPHABET.index(lettre)
    if rang <= 9:
        return '0' + rang
    else:
        return rang

def egcd(a, b):
    if a == 0:  # Paramètre d'arrêt
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)  # Recursif
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m  # Retourne le modulo inverse de 2 nombres s'il existe

def mPrime(lettre, k, e, n) :
    m = rangLettre(str.upper(lettre))
    mP = (m*k**e)%n
    return mP

def mPrimePrime(mP, d, n) :
    mPP = (mP**d)%n
    return mPP

def sFunction(mPP, k, n) :
    return mPP*modinv(k, n)

def dechiffrementSignature(s, e, n) :
    return chr((s**e)%n + 65)