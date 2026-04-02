# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py
from NoeudBinaire import *
from Assets import *

# ==============================================================================

class NoeudHuffman(NoeudBinaire) :
    def __init__( self, v1,v2,v3 ) :
        self.test1 = v1  # Noeud qui est représenté en pratique par un tuple (str "chaine de caractères", int nombre_occurrences)
        self.test2 = v2  # attribut de classe NoeudBinaire qui peut devenir une instance
        self.test3 = v3  # pareil que le gauche.
