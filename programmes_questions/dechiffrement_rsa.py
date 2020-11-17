def decryptRSA(msg, d, n, bloc_size):
    m = ""
    for i in range(0,len(msg)) :
        val = msg[i]
        uncrypted = pow(val, d) % n
        if i == 0 : # On ne complete pas pour le premier indice
            m += str(uncrypted)
        else :
            m += str(uncrypted).zfill(bloc_size)        
    
    ret = ""
    for i in range(0, len(m), 2):
        ret += chr(int(m[i] + m[i+1]) + 65)
    return ret
