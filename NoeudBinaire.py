# C5 - Samuel, Thenujan, Victor
# Fichier NoeudBinaire.py
# from Assets import *
# documentation technique :
# https://fr.wikipedia.org/wiki/Arbre_binaire
# Cours sur les graphes R2.07
# ==============================================================================
class NoeudBinaire() :
# ------------------------------------------------------------------------------
    # Définition du constructeur (unique contrairement au JAVA.) != polymorphisme
    def __init__( self, valeur, gauche = None, droite = None) :
        self.valeur = valeur    # Noeud qui est représenté en pratique par un tuple (str "chaine de caractères", int nombre_occurrences)
        self.gauche = gauche      # attribut de classe NoeudBinaire qui peut devenir une instance
        self.droite = droite      # pareil que le gauche.
    
# Getters / Setters -------------------------------------------------------------
# valeur
    def get_valeur( self ) :
        return self.valeur
    def set_valeur(self,valeur):
        if valeur is None and (self.a_droite() or self.a_gauche()): # racine inexistante ayant au moins une feuille
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
            self.valeur = valeur    # mise à jour du noeud
        
    # gauche
    def get_gauche( self ) :
        return self.gauche
    def set_gauche(self,gauche):
        if self.valeur is None and gauche!=None:
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
            self.gauche = gauche
    
    # droite
    def get_droite( self ) :
        return self.droite
    def set_droite(self,droite):
        if self.valeur is None and droite!=None:
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
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
            haut_g = self.gauche.hauteur() if self.a_gauche() else 0
            haut_d = self.droite.hauteur() if self.a_droite() else 0
            return 1 + max(haut_g,haut_d)
    
    
    def __str__( self ) :
        return self.__str_aux(0)
    
    
    def __str_aux( self, count ) :
        txt = ""
        # racine
        txt += str(self.valeur) + "\n"
        if self.a_gauche() or self.a_droite() :
            # sous-arbre droit
            if self.a_gauche() :
                txt += " " * 5 * count + "|--> "
                txt += self.gauche.__str_aux(count + 1)
            else :
                txt += " " * 5 * count + "|--> " + "\n"
            # sous-arbre gauche
            if self.a_droite() :
                txt += " " * 5 * count + "|--> "
                txt += self.droite.__str_aux(count + 1)
            else :
                txt += " " * 5 * count + "|--> " + "\n"
        return txt
        
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

    # ------------------------------------------------------------------------------

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

    ''' Méthode permettant d'afficher l'ordre de parcours suffixe.'''
    def afficher_suffixe(self):
        if not self.est_vide():
            if self.a_gauche():          # 1. Parcourir le sous-arbre gauche
                self.gauche.afficher_suffixe()
            if self.a_droite():          # 2. Parcourir le sous-arbre droit
                self.droite.afficher_suffixe()
            print(self.valeur, end=' ')  # 3. Visiter la racine
        
    # ------------------------------------------------------------------------------

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
            
# ------------------------------------------------------------------------------
    """
    Parcours largeur (niveau par niveau) de l'arbre binaire:
    Visiter la racine
    Parcourir les noeuds du niveau suivant@return: Liste des valeurs des noeuds dans l'ordre du parcours largeur
    """
    def parcours_largeur( self ) :
        result = [ ]
        if not self.est_vide() :
            queue = [ self ]  # Utilisation d'une file pour le parcours en largeur
            while queue :
                current = queue.pop(0)  # Défilement du noeud courant
                result.append(current.valeur)  # Visiter le noeud courant
                if current.a_gauche() :
                    queue.append(current.gauche)  # Enfiler le fils gauche
                if current.a_droite() :
                    queue.append(current.droite)  # Enfiler le fils droit
        return result
    
    """Méthode permettant d'afficher l'ordre de parcours de l'arbre en ordre largeur."""
    def afficher_largeur( self ) :
        if not self.est_vide() :
            queue = [ self ]  # Utilisation d'une file pour le parcours en largeur
            while queue :
                current = queue.pop(0)  # Défilement du noeud courant
                print(current.valeur, end = ' ')  # Visiter le noeud courant
                if current.a_gauche() :
                    queue.append(current.gauche)  # Enfiler le fils gauche
                if current.a_droite() :
                    queue.append(current.droite)  # Enfiler le fils droit
    # ==============================================================================
