def egcd(a, b):
    if a == 0:  # Paramètre d'arrêt
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)  # Recursif
        return (g, x - (b // a) * y, y)

def inv_mod(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m  # Retourne le modulo inverse de 2 nombres s'il existe

def DechiffreAffine(msg, a, b):
    msg = msg.upper()
    m = ""
    inv = inv_mod(a, 26)
    for cac in msg :
        if cac == " " :
            m += " "
        else :
            letter = ord(cac) - 65
            m += chr(( (inv) * (letter - b )) % 26 + 65)
    return m


Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = 3
b = 10
# CHIFFREMENT AFFINE :
TextClair = "EXECUTE ORDER SIXTY SIX"
chaineDechiffree = ""
for lettre in TextClair:
    if (lettre == " "):
        chaineDechiffree += lettre
    else:
        chaineDechiffree += Alpha[(Alpha.index(lettre)*a + b)%26]

print("CHAINE CHIFFRÉE :\n" + chaineDechiffree)

print(DechiffreAffine(chaineDechiffree, a, b))