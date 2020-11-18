from helper import *
from administrateur import *
from Decompteur import *
from electeur import *
from anonymiseur import *
from commissaire import *

dec = Decompteur(53, 11, 27, 5)

comm = Commissaire()
el1 = Electeur()
el1.ReceiveCode(comm, comm.Distribute())

el2 = Electeur()
el2.ReceiveCode(comm, comm.Distribute())

el3 = Electeur()
el3.ReceiveCode(comm, comm.Distribute())

el4 = Electeur()
el4.ReceiveCode(comm, comm.Distribute())

anon = Anonymiseur()

adm = Administrator()
el1.Vote(anon, dec, adm, comm, "Z")
el2.Vote(anon, dec, adm, comm, "A")
el3.Vote(anon, dec, adm, comm, "B")
el4.Vote(anon, dec, adm, comm, "F")

print(dec.Decompte(anon),comm)