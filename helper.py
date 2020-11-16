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

# Q14
def Hash(msg):
    msg = msg.upper()
    array = []
    blocksize = 16
    for i in range(0, len(msg), blocksize):
        array.append(msg[i:i+blocksize:1].ljust(blocksize, 'A'))
    hash = ""
    for message in array:
        array_1 = []
        for i in range(0, 4):
            val = (ord(message[i]) + ord(message[i+4]) + ord(message[i+8]) + ord(message[i+12]) - 4*65)%26
            array_1.append(val)
        newmsg = ""
        for i in range(0, 16, 4):
            if i == 0: val = message[i+1] + message[i+2] + message[i+3] + message[i]
            if i == 4: val = message[i+2] + message[i+3] + message[i] + message[i+1]
            if i == 8: val = message[i+3] + message[i] + message[i+1] + message[i+2]
            if i == 12: val = message[i+3] + message[i+2] + message[i+1] + message[i]
            newmsg += val
        array_2 = []

        for i in range(0, 4):
            val = (ord(newmsg[i]) + ord(newmsg[i+4]) + ord(newmsg[i+8]) + ord(newmsg[i+12]) - 4*65)%26
            array_2.append(val)
            hash += chr((array_1[i] + val) % 26 + 65)
    return hash

import random
import secrets
import string
alphabet = str.upper(string.ascii_letters)
def Prep():
    N = ''.join(secrets.choice(alphabet) for i in range(12))
    return N