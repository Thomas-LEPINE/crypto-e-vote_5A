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

    def ReceiveElecteurVal(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N:
                self.lst[i].hash = cle.hash
        return

    def Verify(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N and self.lst[i].hash == cle.hash:
                return True
        return False
    def HasVoted(self, cle):
        for i in range(0, len(self.lst)):
            if self.lst[i].N == cle.N and self.lst[i].hash == cle.hash:
                if self.lst[i].voted == True:
                    print("[Commissaire] Electeur a déjà voté !")
                    return False
                self.lst[i].voted = True
                return True
        return False