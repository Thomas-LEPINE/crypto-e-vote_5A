from helper import *
from anonymiseur import *

class Decompteur(object):
    def __init__(self, p, q, e, k):
        self.p = p
        self.q = q
        self.e = e
        self.psy = (self.p - 1) * (self.q - 1)
        self.n, self.d, self.e = RSA(self.p, self.q, self.e)
        self.k = k
        a, b, c = EuclideEtendu(self.k, self.n)
        if(a != 1): print("Not correct k !!")
        else: print("Correct K")
        print(self.p, self.q, self.e, self.psy, self.n, self.d, self.k)

    def Encrypt(self, msg):
        val = encryptRSA(msg, self.n, self.e, 2)
        return val

    def Decompte(self, anon,comm):
        vote_final = []
        for i in anon.votes:
            val = decryptRSA(i, self.d, self.n, 2)
            if comm.VerifyN2(val[1:])
                vote_final.append(val[0])
            else:
                print("Vote ",i," non prit en compte")
        return vote_final