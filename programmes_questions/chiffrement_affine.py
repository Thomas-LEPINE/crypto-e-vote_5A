import string
ALPHABET = str.upper(string.ascii_letters)

def chiffrementAffine(msg, a, b) :
    chaineChiffree = ""
    for lettre in msg:
        if (lettre == " "):
            chaineChiffree += lettre
        else:
            chaineChiffree += ALPHABET[(ALPHABET.index(lettre)*a + b)%26]
    return chaineChiffree