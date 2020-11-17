def decryptRSA(msg, d, n, bloc_size):
    m = ""
    for i in range(0, len(msg)):
        val = msg[i]
        uncrypted = pow(val, d) % n
        m += str(uncrypted).zfill(bloc_size)
    message=""
    array_nb = []
    for i in range(0, len(m), bloc_size):
        message += m[i]
        for j in range(1, bloc_size):
            message += m[i+j]
    ret = ""
    for i in range(0, len(message), 2):
        ret += chr(int(message[i] + message[i+1]) + 65)

    return ret

def decryptRSA2(msgChiffree, d, n, bloc_size):
    Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Chaine de caractère avec toutes les lettre de l'alpabet
    chaineDechiffree = []
    chaineDechiffreeF = ''
    for C in msgChiffree :
        B = (int(C)**d)%n
        chaineDechiffree.append(B)
        chaineDechiffreeF += Alphabet[B]
    return chaineDechiffree, chaineDechiffreeF #Chaine finale en claire
    

print(decryptRSA2([1, 303, 481, 34, 453, 564, 1, 498, 127, 115], 347, 583, 3))
