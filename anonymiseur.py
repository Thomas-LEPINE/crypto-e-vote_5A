from commissaire import *

class Anonymiseur(object):
    def __init__(self):
        self.votes = []
        return

    def ReceiveVote(self):
        print('Entrez le vote:')
        vote=input()
        self.votes.append(vote)