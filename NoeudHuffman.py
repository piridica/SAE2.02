# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py
from NoeudBinaire import *
from Assets import *

# ==============================================================================

class NoeudHuffman(NoeudBinaire):
    def __init__(self, chaine, poids, gauche=None, droite=None):
        super().__init__((chaine, poids), gauche, droite)

    @staticmethod
    def depuis_chaine(chaine):
        dico = nb_ocurrences(chaine)
        noeuds = [NoeudHuffman(c, p) for c, p in dico.items()]
        while len(noeuds) > 1:
            noeuds.sort(key=lambda x: x.valeur[1])
            g = noeuds[0]
            d = noeuds[1]
            parent = NoeudHuffman(
                g.valeur[0] + d.valeur[0],
                g.valeur[1] + d.valeur[1],
                g,
                d
            )
            noeuds = [parent] + noeuds[2:]
        return noeuds[0]

    def encodage(self, prefixe=""):
        if self.est_feuille():
            return {self.valeur[0]: prefixe if prefixe != "" else "0"}
        codes = {}
        if self.gauche:
            codes.update(self.gauche.encodage(prefixe + "0"))
        if self.droite:
            codes.update(self.droite.encodage(prefixe + "1"))
        return codes

    def compresser(self, chaine, codes):
        return "".join(codes[c] for c in chaine)

    def decompresser(self, chaine_compressee):
        chaine_decodee = ""
        courant = self
        for bit in chaine_compressee:
            if bit == "0":
                courant = courant.gauche
            else:
                courant = courant.droite
            if courant.est_feuille():
                chaine_decodee += courant.valeur[0]
                courant = self
        return chaine_decodee
