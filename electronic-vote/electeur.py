from helper import *
from administrateur import *

class Electeur(object):
    def __init__(self):
        return

    def ReceiveCode(self, commissaire, code):
        self.n1 = code
        self.n2 = Prep()
        self.vc = None
        self.n1.SetHash(Hash(self.n2))
        commissaire.ReceiveElecteurVal(self.n1)

    def Vote(self, anon, dec, admin, comm, vote):
        if admin.Contact(self.n1, comm):
            print("Code valid !")
            self.vote = vote + self.n2

            # Validate blind signature
            newm = []
            for i in range(0, len(self.vote)):
                val = (ord(self.vote[i]) - 65) % 26
                mp = val * pow(admin.dec.k, admin.dec.e) % admin.dec.n
                newm.append(mp)
            mpp = admin.BlindSign(newm)

            for i in range(0, len(mpp)):
                (kinv, u, v) = EuclideEtendu(admin.dec.k, admin.dec.n)
                kinv = u % admin.dec.n
                s = (mpp[i] * kinv) % admin.dec.n
                if(pow(s, admin.dec.e)%admin.dec.n != (ord(self.vote[i]) - 65)):
                    print("COULD NOT VALIDATE SIGNATURE (i=" + str(i) + ")")
                    return
            print("[Electeur] Signature validée !")

            self.vc = dec.Encrypt(self.vote)
            print(self.vc)
            anon.ReceiveVote(self.n1, self.vc, comm)
            return
        else:
            print("Code not valid!")
            return