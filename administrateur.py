from helper import *
from Decompteur import *

class Administrator(object):
    def __init__(self):
        self.dec = Decompteur(53, 11, 27, 5)
        return

    '''
    Prends le commissaire et lui demande de verifier la clé
    Dit Oui si peut voter, sinon non
    '''
    def Contact(self):
        print ("La clé est : ")
        cle=input()
        print ("La commissaire est : ")
        commissaire=input()
        #return commissaire.Verify(cle)
        print("Le commissaire est : ", commissaire)
        print("La clé est : ", cle)

    '''
    Signe le mp
    '''
    def BlindSign(self):
        mp = InputArray("Le mp est : ")
        array = []
        for i in range(0, len(mp)):
            array.append(pow(mp[i], self.dec.d) % self.dec.n)
        print("Le mpp est : ", array)

#Test

admin=Administrator()
com1=Commissaire()
admin.Contact()
admin.BlindSign()

