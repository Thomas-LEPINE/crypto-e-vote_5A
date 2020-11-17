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

def blockSize(n):
    blocksize = 0
    nF = n
    while nF >= 10:
        nF = int(nF/10)
        blocksize += 1
    return blocksize

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

n, d, e = RSA(53, 11, 3)
print(RSA(53, 11, 3))
print(encryptRSA("POLYTECHANGERS", n, e, blockSize(n)+1))