# C5 - Samuel, Thenujan, Victor
# Fichier NoeudBinaire.py
from Assets import *
# documentation technique :
# https://fr.wikipedia.org/wiki/Arbre_binaire
# Cours sur les graphes R2.07
# ==============================================================================
class NoeudBinaire() :

# ------------------------------------------------------------------------------
    # Définition du constructeur (unique contrairement au JAVA.) != polymorphisme
    def __init__( self, valeur ) :
        self.valeur = valeur    # Noeud qui est représenté en pratique par un tuple (str "chaine de caractères", int nombre_occurrences)
        self.gauche = None      # attribut de classe NoeudBinaire qui peut devenir une instance
        self.droite = None      # pareil que le gauche.
    
    
# Getters / Setters -------------------------------------------------------------
# valeur
    def get_valeur( self ) :
        return self.valeur
    def set_valeur( self, valeur ) :
        if valeur == None and self.valeur != None :  # vérifie que valeur et self.valeur sont différents
            if self.gauche != None or self.droite != None :  # vérifie si l'un des sous-arbres n'est pas vide
                raise ExpectionError("Vous ne pouvez pas supprimer un noeud ayant des sous-noeuds!")
        else :
            self.valeur = valeur  # mise à jour du noeud
    
    # gauche
    def get_gauche( self ) :
        return self.gauche
    def set_gauche( self, gauche ) :
        self.gauche = gauche
    
    # droite
    def get_droite( self ) :
        return self.droite
    def set_droite( self, droite ) :
        self.droite = droite
    
    # ------------------------------------------------------------------------------
    # Fonctions responsables de la vérification de l'état des noeuds, et des sous-noeuds
    # noeud vide
    def est_vide( self ) :
        return self.valeur is None
    # Vérifie que le noeud n'a ni de fils gauche ni de fils droit.
    def est_feuille(self):
        return self.valeur!=None and self.gauche==None and self.droite==None
    # Vérification de l'existence d'un fils gauche
    def a_gauche(self):
        return self.gauche!=None
    # et droit
    def a_droite(self):
        return self.droite!=None

    def hauteur(self):
        if self.est_vide():
            return 0
        else:
            return max(gauche.hauteur(),droite.hauteur())
    # ------------------------------------------------------------------------------

# ==============================================================================
    """
    Parcours préfixe (préordre) de l'arbre binaire:
    1. Visiter la racine
    2. Parcourir le sous-arbre gauche
    3. Parcourir le sous-arbre droit
    @return: Liste des valeurs des noeuds dans l'ordre du parcours préfixe
    """
    def parcours_prefixe(self):
        result = []
        # 1. Visiter la racine (ajouter la valeur du noeud courant)
        if not self.est_vide():
            result.append(self.valeur)
            # 2. Parcourir le sous-arbre gauche si existe
            if self.a_gauche():
                result.extend(self.gauche.parcours_prefixe())
            # 3. Parcourir le sous-arbre droit si existe
            if self.a_droite():
                result.extend(self.droite.parcours_prefixe())
        return result

    ''' Méthode permettant d'afficher l'ordre de parcours de l'arbre en ordre préfixe.'''
    def afficher_prefixe(self):
        """
        Affiche les valeurs des noeuds dans l'ordre du parcours préfixe
        """
        if not self.est_vide():
            print(self.valeur, end=' ')  # 1. Visiter la racine
            if self.a_gauche():          # 2. Parcourir le sous-arbre gauche
                self.gauche.afficher_prefixe()
            if self.a_droite():          # 3. Parcourir le sous-arbre droit
                self.droite.afficher_prefixe()

    """Parcours suffixe (postordre) de l'arbre binaire:
    1. Parcourir le sous-arbre gauche
    2. Parcourir le sous-arbre droite
    3. Visiter la racine
    @return: Liste des valeurs des noeuds dans l'ordre du parcours suffixe"""
    def parcours_suffixe(self):     # Visiter les noeuds d'un arbre binaire en suffixe (postfixe)
        result = []
        if not self.est_vide():             # 1. Parcourir le sous-arbre gauche si existe
            if self.a_gauche():
                result.extend(self.gauche.parcours_suffixe())
            if self.a_droite():              # 2. Parcourir le sous-arbre droit si existe
                result.extend(self.droite.parcours_suffixe())
            result.append(self.valeur)      # 3. Visiter la racine (ajouter la valeur du noeud courant)
        return result

    ''' Méthode permettant d'afficher l'ordre de parcours de l'arbre en ordre suffixe.'''
    def afficher_suffixe(self):
        """
        Affiche les valeurs des noeuds dans l'ordre du parcours suffixe
        """
        if not self.est_vide():
            if self.a_gauche():          # 1. Parcourir le sous-arbre gauche
                self.gauche.afficher_suffixe()
            if self.a_droite():           # 2. Parcourir le sous-arbre droit
                self.droite.afficher_suffixe()
            print(self.valeur, end=' ')  # 3. Visiter la racine

    """
    Parcours infixe (en ordre) de l'arbre binaire :
    1. Sous-arbre gauche
    2. Racine
    3. Sous-arbre droit
    @return: Liste des valeurs des nœuds dans l'ordre du parcours infixe
    """
    def parcours_infixe( self ) :
        result = [ ]
        if self.gauche :  # 1. Parcourir le sous-arbre gauche
            result += self.gauche.parcours_infixe()
        result.append(self.valeur)  # 2. Visiter la racine
        if self.droite :  # 3. Parcourir le sous-arbre droit
            result += self.droite.parcours_infixe()
        return result


    """Affiche les valeurs des nœuds dans l'ordre du parcours infixe"""
    def afficher_infixe( self ) :

            if self.gauche :  # 1. Sous-arbre gauche
                self.gauche.afficher_infixe()
            print(self.valeur, end = ' ')  # 2. Racine
            if self.droite :  # 3. Sous-arbre droit
                self.droite.afficher_infixe()
    # ==============================================================================
