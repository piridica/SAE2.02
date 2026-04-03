# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py
from NoeudBinaire import *
from Assets import *

# ==============================================================================

class NoeudHuffman(NoeudBinaire) :
    def __init__( self, chaine, poids, gauche=None, droite=None ) :
        super().__init__((chaine, poids), gauche, droite)  # appel du constructeur de la classe parent NoeudBinaire
        

    @staticmethod
    #def depuis_chaine( chaine ) :
    def depuis_chaine(chaine):
        dico = nb_ocurrences(chaine)  # dico = { 'caractère' : nb_occurences, ... }
        noeuds = [NoeudHuffman(caractere, poids) for caractere, poids in dico.items()]  # liste de NoeudHuffman pour chaque caractère distinct
        while len(noeuds) > 1:
            noeuds.sort(key=lambda x: x.valeur[1])  # tri par poids (nombre d'occurrences)
            gauche = noeuds[0]  # noeud avec le plus petit poids
            droite = noeuds[1]  # noeud avec le deuxième plus petit poids
            nouveau_noeud = NoeudHuffman(gauche.valeur[0] + droite.valeur[0], gauche.valeur[1] + droite.valeur[1], gauche, droite)  # création d'un nouveau noeud parent
            noeuds = [nouveau_noeud] + noeuds[2:]  # mise à jour de la liste des noeuds
        return noeuds[0]  # retourne la racine de l'arbre de Huffman

    #def encodage(self, prefixe=""):
    def encodage(self, prefixe=""):
        if self.est_feuille():
            return {self.valeur[0]: prefixe}  # retourne un dictionnaire avec le caractère et son code binaire
        else:
            code_gauche = self.gauche.encodage(prefixe + "0") if self.gauche else {}
            code_droite = self.droite.encodage(prefixe + "1") if self.droite else {}
            return {**code_gauche, **code_droite}  # fusionne les deux dictionnaires

    #def compresser (self, chaines, codes):
    def compresser(self, chaines, codes):
        texte_compresse = ""
        for caractere in chaines:
            texte_compresse += codes[caractere]  # remplace chaque caractère par son code binaire
        return texte_compresse
