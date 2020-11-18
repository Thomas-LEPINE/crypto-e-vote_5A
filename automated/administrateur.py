from helper import *
from Decompteur import *
class Administrator(object):
    def __init__(self):
        self.dec = Decompteur(53, 11, 27, 5)
        return
    def Contact(self, cle, commissaire):
        return commissaire.Verify(cle)
    def BlindSign(self, mp):
        array = []
        for i in range(0, len(mp)):
            array.append(pow(mp[i], self.dec.d) % self.dec.n)
        return array