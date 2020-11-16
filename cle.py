from helper import *
class Cle(object):
    def __init__(self):
        self.N = Prep()
        self.hash = None
        self.voted = False
        return
    def SetHash(self, hash):
        self.hash = hash

    def __str__(self):
        return "[clé=" + self.N + ", hash=" + self.hash + "]"