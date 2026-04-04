# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py
from NoeudBinaire import *
from Assets import *

# ==============================================================================

class NoeudHuffman(NoeudBinaire):
    def __init__(self, chaine, poids, gauche=None, droite=None):
        super().__init__((chaine, poids), gauche, droite)  # la valeur du noeud est un tuple (chaine, poids)

    @staticmethod
    def depuis_chaine(chaine):
        dico = nb_ocurrences(chaine)                            # compte combien de fois chaque caractère apparaît
        noeuds = [NoeudHuffman(c, p) for c, p in dico.items()]  # crée une feuille par caractère distinct
        while len(noeuds) > 1:                                  # on fusionne jusqu'à n'avoir qu'un seul arbre
            noeuds.sort(key=lambda x: x.valeur[1])              # trie par poids croissant (le plus léger en premier)
            g = noeuds[0]                                       # noeud avec le plus petit poids
            d = noeuds[1]                                       # noeud avec le deuxième plus petit poids
            parent = NoeudHuffman(
                g.valeur[0] + d.valeur[0],                      # concatène les chaînes des deux noeuds
                g.valeur[1] + d.valeur[1],                      # additionne leurs poids
                g,                                              # fils gauche
                d                                               # fils droit
            )
            noeuds = [parent] + noeuds[2:]                      # remplace les deux noeuds fusionnés par leur parent
        return noeuds[0]                                        # retourne la racine de l'arbre de Huffman

    def encodage(self, prefixe=""):
        if self.est_feuille():
            return {self.valeur[0]: prefixe if prefixe != "" else "0"}    # cas limite : arbre avec un seul caractère, code = "0"
        codes = {}
        if self.gauche:
            codes.update(self.gauche.encodage(prefixe + "0"))             # branche gauche alors on ajoute "0" au préfixe
        if self.droite:
            codes.update(self.droite.encodage(prefixe + "1"))             # branche droite alors on ajoute "1" au préfixe
        return codes                                                      # retourne le dictionnaire { caractère : code binaire }

    def compresser(self, chaine, codes):
        return "".join(codes[c] for c in chaine)                          # remplace chaque caractère par son code binaire

    def decompresser(self, chaine_compressee):
        chaine_decodee = ""
        courant = self                                                    # on part de la racine
        for bit in chaine_compressee:                                     # on lit bit par bit
            if bit == "0":
                courant = courant.gauche                                  # si "0" alors on va à gauche
            else:
                courant = courant.droite                                  # si "1" alors on va à droite
            if courant.est_feuille():                                     # si on arrive sur une feuille
                chaine_decodee += courant.valeur[0]                       # on récupère le caractère
                courant = self                                            # on repart de la racine pour le caractère suivant
        return chaine_decodee
    
#====================================================================
