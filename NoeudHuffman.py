# C5 - Samuel, Thenujan, Victor
# Fichier NoeudHuffman.py

from NoeudBinaire import *

# ==============================================================================
# === CLASSE NOEUDHUFFMAN ======================================================
# ==============================================================================

class NoeudHuffman(NoeudBinaire) :
    
    def __init__(self,valeur,gauche=None,droite=None) :
        """
        params:
            valeur: ici ce sera un tuple (char,int), il faudra le vérifier
        """
        
        if not isinstance(valeur,tuple):
            raise TypeError("valeur doit être un tuple")
        if len(valeur) != 2:
            raise ValueError("valeur doit être de taille 2")
            
        s,es=valeur
        if not isinstance(s,str):
            raise TypeError("le 1er élément doit être un caractère")
        if not isinstance(es,int):
            raise TypeError("le 2e élément doit être un entier")
            
        super().__init__(valeur,gauche,droite)
    
    def poids(self):
        """
        Retourne le poids du couple (chaine,poids) contenu dans la racine de l'arbre
        """
        return self.valeur[1]

    def chaine(self):
        """
        Retourn la chaine du couple (chaine,poids) contenu dans la racine de l'arbre
        """
        return self.valeur[0]
    
    @staticmethod
    def feuillesHuffman(chaine):
        """
        Renvoie le dictionnaire des feuilles de l'arbre d'Huffman {str:int}
        
        On utilise un dictionnaire car le dictionnaire utilise une hashtable ce qui 
        demande une complexité de O(1) pour la recherche d'élement tandis qu'une liste
        aura besoin d'une complexité en O(n).
        """
        dico = {}
        for c in chaine:
            if c in dico :
                dico[c] += 1
            else :
                dico[c] = 1
        
        return dico

    @staticmethod
    def construire_huffman(chaine):
        """
        Renvoie l'arbre de Huffman associé à la chaîne de caractères donné en paramètre
        """
        feuilles = NoeudHuffman.feuillesHuffman(chaine)
        noeuds = [NoeudHuffman((c, occ)) for c,occ in feuilles.items()]
        # tri initial
        noeuds.sort(key=lambda n: (n.poids(), n.chaine()))

        while len(noeuds) > 1:
            # prendre les 2 plus petits
            gauche = noeuds.pop(0)
            droite = noeuds.pop(0)

            # fusion
            nouvelle_chaine = gauche.chaine() + droite.chaine()
            nouveau_poids = gauche.poids() + droite.poids()

            parent = NoeudHuffman((nouvelle_chaine, nouveau_poids), gauche, droite)

            # ajouter et re-trier
            noeuds.append(parent)
            noeuds.sort(key=lambda n: (n.poids(), n.chaine()))

        return noeuds[0]  # racine

    def encodage(self, prefixe=""):
        """
        Renvoie le dictionnaire des caractères associés à leur encodage {caractère:code}
        """
        if self.est_feuille():
            return {self.valeur[0]: prefixe if prefixe != "" else "0"}
        codes = {}
        if self.gauche:
            codes.update(self.gauche.encodage(prefixe + "0"))
        if self.droite:
            codes.update(self.droite.encodage(prefixe + "1"))
        return codes

    def compresser(self, chaine, codes):
        """
        Renvoie la chaine de bits correspondant à la compression de la chaine en paramètre selon l'encodage donné
        """
        return "".join(codes[c] for c in chaine)

    def decompresser(self, chaine_compressee):
        """
        Renvoie la chaine décompressée à partir de celle compressée selon l'arbre d'Huffman appelé
        """
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

