from helper import *
from anonymiseur import *
from commissaire import *
from administrateur import *
from electeur import *

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

    def Decompte(self):#, anon):
        nbvote=int(input("Nombre de votes a tester : "))
        votes=[]
        for i in range(0,nbvote):
            votetemp=InputArray("Saisir le vote : \n")
            votes.append(votetemp)
        for i in votes:
            val = decryptRSA(i,self.d,self.n,2)
            print(val)
        '''
        for i in anon.votes:
            val = decryptRSA(i, self.d, self.n, 2)
            print(val)
        '''
        return

#Test classe

dec=Decompteur(53,11,27,5)
msg=input("Test msg encrypt : ")
msg_encrypt=dec.Encrypt(msg)
print(msg_encrypt)

dec.Decompte()


'''
anon = Anonymiseur()
comm = Commissaire()
el1 = Electeur()
el1.ReceiveCode(comm, comm.Distribute())
nb_votes=input("Combien de vote a saisir ? ")
for i in range(0,int(nb_votes)):
    N1=input("Saisir N1 du vote : ")
    vc=input("Saisir cv du vote : ")
    vc=str.upper(vc)
    anon.ReceiveVote(N1,vc,comm)

dec.Decompte(anon)

'''