from helper import *
from cle import *

class Commissaire(object):
    def __init__(self):
        self.lst = []
        self.distributed = 0
        for i in range(0, 20):
            self.lst.append(Cle())
        return

    def Distribute(self):
        val = self.lst[self.distributed]
        self.distributed += 1
        return val

    def ReceiveElecteurVal(self):
        print('Entrez N1:')
        N = input()
        print('Entrez le Hash:')
        hash = input()
        for i in range(0, len(self.lst)):
            if self.lst[i].N == N:
                self.lst[i].hash = hash
        return

    def Verify(self):
        print('Entrez N1:')
        N = input()
        print('Entrez le Hash:')
        hash = input()
        for i in range(0, len(self.lst)):
            if self.lst[i].N == N and self.lst[i].hash == hash:
                return True
        return False

    def HasVoted(self):
        print('Entrez N1:')
        N = input()
        print('Entrez le Hash:')
        hash = input()
        for i in range(0, len(self.lst)):
            if self.lst[i].N == N and self.lst[i].hash == hash:
                if self.lst[i].voted == True:
                    print("[Commissaire] Electeur a déjà voté !")
                    return False
                self.lst[i].voted = True
                return True
        return False
