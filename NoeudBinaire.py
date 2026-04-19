# C5 - Samuel, Thenujan, Victor
# Fichier NoeudBinaire.py

# Documentation technique :
# https://fr.wikipedia.org/wiki/Arbre_binaire
# Cours sur les graphes R2.07

# ==============================================================================
# === CLASSE NOEUDBINAIRE ======================================================
# ==============================================================================

class NoeudBinaire() :

    def __init__( self, valeur, gauche = None, droite = None) :
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
    
    # --- GETTERS, SETTERS ---------------------------------------------

    def get_valeur( self ) :
        """
        Renvoie la valeur de la racine de l'arbre
        """
        return self.valeur
        
    def set_valeur(self,valeur):
        """
        Modifie la valeur de la racine de l'arbre
        """
        if valeur is None and (self.a_droite() or self.a_gauche()): # racine inexistante ayant au moins une feuille
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
            self.valeur = valeur    # mise à jour du noeud
        
    def get_gauche( self ):
        """
        Renvoie le sous-arbre gauche
        """
        return self.gauche
        
    def set_gauche(self,gauche):
        """
        Modifie le sous-arbre gauche
        Raises:
            ValueError: si la racine est vide et le noeud non vide
        """
        if self.valeur is None and gauche!=None:
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
            self.gauche = gauche
    
    def get_droite( self ) :
        return self.droite
        
    def set_droite(self,droite):
        """
        Modifie le sous-arbre droit
        Raises:
            ValueError: si la racine est vide et le noeud non vide
        """
        if self.valeur is None and droite!=None:
            raise ValueError("Noeud enfant d'une racine qui n'existe pas")
        else:
            self.droite = droite
    
    # --- METHODES -----------------------------------------------------
    
    def est_vide( self ) :
        """
        Vérifie si l'arbre est vide (il suffit de vérifier que la racine est vide car alors il n'y a pas de sous-arbres)
        """
        return self.valeur is None
        
    def est_feuille(self):
        """
        Vérifie que l'arbre est une racine sans sous-arbre gauche ou droit, c'est à dire une feuille
        """
        return self.valeur!=None and self.gauche==None and self.droite==None
        
    def a_gauche(self):
        """
        Vérifie que l'arbre possède un sous-arbre gauche (non vide)
        """
        return self.gauche!=None

    def a_droite(self):
        """
        Vérifie que l'arbre possède un sous-arbre droite (non vide)
        """
        return self.droite!=None

    def hauteur(self):
        """
        Calcule la hauteur de l'arbre par rapport à ses noeuds
        """
        if self.est_vide():
            return 0
        else:
            haut_g = self.gauche.hauteur() if self.a_gauche() else 0
            haut_d = self.droite.hauteur() if self.a_droite() else 0
            return 1 + max(haut_g,haut_d)
    
    
    def __str__( self ) :
        """
        Affiche l'arbre sous forme horizontale en faisant appel à une fonction récursive auxiliaire
        """
        return self.__str_aux(0)
    
    
    def __str_aux( self, count ) :
        """
        Affiche l'arbre sous forme horizontale récursivement jusqu'à afficher l'arbre du premier appel en entier
        """
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
        
    # --- METHODES: PARCOURS -------------------------------------------
    
    def parcours_prefixe(self):
        """
        Parcours préfixe (préordre) de l'arbre binaire:
        1. Visiter la racine
        2. Parcourir le sous-arbre gauche
        3. Parcourir le sous-arbre droit
        @return: Liste des valeurs des noeuds dans l'ordre du parcours préfixe
        """
        result = []
        if not self.est_vide():
            result.append(self.valeur)
            if self.a_gauche():
                result.extend(self.gauche.parcours_prefixe())
            if self.a_droite():
                result.extend(self.droite.parcours_prefixe())
        return result

    def parcours_suffixe(self):
        """Parcours suffixe (postordre) de l'arbre binaire:
        1. Parcourir le sous-arbre gauche
        2. Parcourir le sous-arbre droite
        3. Visiter la racine
        @return: Liste des valeurs des noeuds dans l'ordre du parcours suffixe"""
        result = []
        if not self.est_vide():
            if self.a_gauche():
                result.extend(self.gauche.parcours_suffixe())
            if self.a_droite():
                result.extend(self.droite.parcours_suffixe())
            result.append(self.valeur)
        return result

    def parcours_infixe( self ) :
        """
        Parcours infixe (en ordre) de l'arbre binaire :
        1. Sous-arbre gauche
        2. Racine
        3. Sous-arbre droit
        @return: Liste des valeurs des nœuds dans l'ordre du parcours infixe
        """
        result = [ ]
        if self.gauche :
            result += self.gauche.parcours_infixe()
        result.append(self.valeur)
        if self.droite :
            result += self.droite.parcours_infixe()
        return result

    def parcours_largeur( self ) :
        """
        Parcours largeur (niveau par niveau) de l'arbre binaire:
        1. Visiter la racine
        2. Parcourir les noeuds du niveau suivant
        @return: Liste des valeurs des noeuds dans l'ordre du parcours largeur
        """
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


