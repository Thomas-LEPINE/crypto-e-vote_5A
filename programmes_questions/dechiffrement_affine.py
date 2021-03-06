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

def dechiffreAffine(msg, a, b):
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