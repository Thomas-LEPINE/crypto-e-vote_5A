from helper import *
from administrateur import *

class Electeur(object):
    def __init__(self):
        return

    # def ReceiveCode(self, commissaire, code):
    def ReceiveCode(self):
        #self.n1 = code
        n1 = input("Entrez le code N1: ")
        self.n1 = Cle()
        self.n1.N = n1
        self.n2 = Prep()
        self.vc = None
        self.n1.SetHash(Hash(self.n2))
        print("Pret à envoyer N1: " + str(self.n1))
        #commissaire.ReceiveElecteurVal(self.n1)

    #def Vote(self, anon, dec, admin, comm, vote):
    def Vote(self):
        #if admin.Contact(self.n1, comm):
            vote = input("Entrez votre vote: ")
            print("Code valid !")
            self.vote = vote + self.n2

            k = int(input("Entrez k: "))
            e = int(input("Entrez e: "))
            n = int(input("Entrez n: "))

            # Validate blind signature
            newm = []
            for i in range(0, len(self.vote)):
                val = (ord(self.vote[i]) - 65) % 26
                mp = val * pow(k, e) % n
                newm.append(mp)
            print("m' = " + str(newm))
#[0, 515, 256, 324, 379, 13, 366, 528, 0, 541, 94, 324, 13]
            mpp = InputArray("Entrez mpp")

            #for i in range(0, len(newm)):
            #    mpp.append(int(input("Entrez m''[" + str(i) + "]: ")))
            #mpp = admin.BlindSign(newm)

            for i in range(0, len(mpp)):
                (kinv, u, v) = EuclideEtendu(k, n)
                kinv = u % n
                s = (mpp[i] * kinv) % n
                if(pow(s, e)%n != (ord(self.vote[i]) - 65)):
                    print("COULD NOT VALIDATE SIGNATURE (i=" + str(i) + ")")
                    #return # for the moment, comment it
            print("[Electeur] Signature validée !")

            print("Pret à chiffrer le vote: " + str(self.vote))
            #array = input("Entrez le vote chiffré: ")
            self.vc = InputArray("Entrez le vote chiffré :")
            print(self.vc)
            #self.vc = dec.Encrypt(self.vote)
            #print(self.vc)
            print("Prêt pour recevoir le vote: n1 = " + str(self.n1) + ", vote= " + str(self.vc))
            #anon.ReceiveVote(self.n1, self.vc, comm)
            return
        #else:
        #    print("Code not valid!")
        #    return

#print(InputArray("test : "))

dec = Decompteur(53, 11, 27, 5)
print(dec.n)

el = Electeur()
el.ReceiveCode()
el.Vote()