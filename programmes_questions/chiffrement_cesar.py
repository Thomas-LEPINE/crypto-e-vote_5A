def cesar(m, k):
    m = m.upper()
    msg = ""
    for cac in m :
        if(cac == " ") :
            msg += cac
        else :
            msg += chr(((ord(cac) - 65) + k)%26 + 65)
    return msg