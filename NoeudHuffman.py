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
            
        c,e=valeur
        if not isinstance(c,str):
            raise TypeError("le 1er élément doit être un caractère")
        if not isinstance(e,int):
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

    # --- METHODES: SERIALISATION ----------------------------------------------
 
    def serialiser(self):
        """
        Sérialise l'arbre de Huffman en une chaîne de caractères (parcours préfixe) :
        - Nœud interne → '0'
        - Feuille       → '1' + le caractère
        Cette chaîne permet de reconstruire l'arbre exactement à l'identique.
        Le séparateur § étant hors ASCII et unidecode() ne le produisant jamais,
        aucun échappement n'est nécessaire.
        """
        if self.est_feuille():
            return "1" + self.valeur[0]
        else:
            gauche_ser = self.gauche.serialiser() if self.a_gauche() else ""
            droite_ser = self.droite.serialiser() if self.a_droite() else ""
            return "0" + gauche_ser + droite_ser
 
    @staticmethod
    def deserialiser(chaine, index=0):
        """
        Reconstruit un arbre de Huffman depuis une chaîne sérialisée.
        @param chaine : la chaîne produite par serialiser()
        @param index  : position courante dans la chaîne (pour la récursion)
        @return       : (NoeudHuffman reconstruit, nouvel index)
        """
        if index >= len(chaine):
            raise ValueError("Chaîne sérialisée invalide ou tronquée.")
 
        type_noeud = chaine[index]
        index += 1
 
        if type_noeud == "1":
            c = chaine[index]
            index += 1
            return NoeudHuffman((c, 0)), index
 
        else:  # type_noeud == "0" → nœud interne
            gauche, index = NoeudHuffman.deserialiser(chaine, index)
            droite, index = NoeudHuffman.deserialiser(chaine, index)
            chaine_fusionnee = gauche.chaine() + droite.chaine()
            return NoeudHuffman((chaine_fusionnee, 0), gauche, droite), index
