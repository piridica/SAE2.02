# C5 - Samuel, Thenujan, Victor
# Fichier NoeudBinaire.py

# documentation technique :
# https://fr.wikipedia.org/wiki/Arbre_binaire
# Cours sur les graphes R2.07
# ==============================================================================

class NoeudBinaire():
"""
    # définition d'un arbre vide
    v_noeud = None      # Noeud qui est représenté en pratique par un tuple (str "chaine de caractères", int nombre_occurrences)
    fils_g = None       # attribut de classe NoeudBinaire qui peut devenir une instance
    fils_d = None       # pareil que le gauche.
"""
# ------------------------------------------------------------------------------
    # Définition du constructeur (unique contrairement au JAVA.) != polymorphisme
    def __init__( self, v_noeud, fils_g = None, fils_d = None ):
        self.v_noeud = v v_noeud
        self.fils_g = fils_g
        self.fild_d = fils_d
        
        
        
    