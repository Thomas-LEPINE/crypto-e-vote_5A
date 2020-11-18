from commissaire import *

class Anonymiseur(object):
    def __init__(self):
        self.votes = []
        return

    def ReceiveVote(self, cle, vote, commissaire):
        if(not commissaire.HasVoted(cle)):
            print("[Anonymiseur] La vérification de la clé a échoué.")
            return
        self.votes.append(vote)