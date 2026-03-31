# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py
from NoeudBinaire import *
# ==============================================================================

class NoeudHuffman(NoeudBinaire):
    def __init__(self, symbole=None, frequence=0):
        self.symbole = symbole      #None si noeud interne, un caractère
        self.frequence = frequence  #nombre d'occurrences du symbole dans le texte à compresser
        self.gauche = None          #enfant gauche du noeud
        self.droit = None           #enfant droit du noeud

    #Nécessaire pour heapq : compare deux noeuds par fréquence
    def __lt__(self, autre) :
        return self.frequence < autre.frequence
    
    def est_feuille(self) : 
        return self.gauche is None and self.droit is None
    
    def __repr__(self):
        return f"Noeud(sym={self.symbole!r}, freq={self.frequence})"

# ==============================================================================
# En cours de développement : fonctions pour construire l'arbre de Huffman à partir d'un texte
def car_distincts(texte):
    """Retourne les caractères distincts et leurs occurrences dans un texte."""
    if not isinstance(texte, str):
        raise TypeError("car_distincts attend une chaîne de caractères")
    dico = {}
    for c in texte:
        dico[c] = dico.get(c, 0) + 1
    return dico


def nb_occurences(txt):
    """Alias de car_distincts pour compatibilité."""
    return car_distincts(txt)
