from commissaire import *

class Anonymiseur(object):
    def __init__(self):
        self.votes = []
        return

    def ReceiveVote(self):
        print('Entrez le vote:')
        vote=input()
        if self.verifN1() == True :
            self.votes.append(vote)
        else :
            print("C'est mort")
           
    def verifN1() :
        Commissaire.Verify()
        return True