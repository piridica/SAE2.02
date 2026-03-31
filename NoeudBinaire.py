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
        self.v_noeud = v_noeud
        self.fils_g = fils_g
        self.fild_d = fils_d
        
# Getters / Setters -------------------------------------------------------------
# v_noeud
    def get_v_noeud(self):
        return self.v_noeud
    def set_v_noeud(self,v_noeud):
        if v_noeud == None and self.v_noeud != None :       # vérifie que v_noeud et self.v_noeud sont différents
            if self.fils_g != None or self.fils_d != None : # vérifie si l'un des sous-arbres n'est pas vide
                raise ExpectionError("Vous ne pouvez pas supprimer un noeud ayant des sous-noeuds!")
        else :
            self.v_noeud = v_noeud  # mise à jour du noeud
# fils_g
    def get_fils_g(self):
        return self.fils_g
    def set_fils_g(self,fils_g):
        self.fils_g = fils_g
# fils_d
    def get_fils_d(self):
        return self.fils_d
    def set_fils_d(self,fils_d):
        self.fils_d = fils_d
# ------------------------------------------------------------------------------
# Fonctions responsables de la vérification de l'état des noeuds, et des sous-noeuds
# noeud vide
    def vide(self):
        return self.v_noeud is None
# Vérifie que le noeud n'a ni de fils gauche ni de fils droit.
    def feuille(self):
        return self.v_noeud!=None and self.fils_g==None and self.fil_d==None

# Vérification de l'existence d'un fils gauche
    def existe_arbre_g(self):
        return self.fils_g!=None
# et droit
    def existe_arbre_d(self):
        return self.fils_d!=None
# ------------------------------------------------------------------------------
'''
@arguments : poids du fichier initial, puis celui du fichier encodé
@return : taux de compression en %
Etat de développement : fini, non testé
'''
    def taux_compression(mem_txt,mem_txt_encode):
        return ((mem_txt-mem_txt_encode)/mem_txt)*100   # à voir s'il vaut mieux conserver le *100 ou pas. les deux se vallent
    
'''
@arguments : chemin d'accès et nom du fichier à peser
@return : poids du fichier concerné
@errors : fichier n'existe pas à cet emplacement
Etat de développement : fini, non testé
'''
    def get_file_size( nom_fichier ) :
        # Vérifie si le fichier existe pour éviter les erreurs
        if os.path.isfile(nom_fichier) :
            size = os.path.getsize(nom_fichier)
            print(f"Taille du fichier : {size} octets")
            return size
        else :
            raise FileNotFoundError(f"Le fichier '{nom_fichier}' n'existe pas.")

'''
@arguments : nom_dossier
Méthode permettant d'afficher dans la console le poids de fichiers stockés dans un certain répertoire
Etat de développement : fini, non testé
'''
    def affiche_size( nom_dossier ) :
        # Liste tous les éléments du dossier
        for nom_fichier in os.listdir(nom_dossier) :
            chemin_complet = os.path.join(nom_dossier, nom_fichier)
            # Vérifie que c'est bien un fichier (pas un sous-dossier)
            if os.path.isfile(chemin_complet) :
                # Récupère la taille en octets
                taille = os.path.getsize(chemin_complet)
                print(f"Le fichier : {nom_fichier} pèse {taille} octets")
'''
@arguments : chemin d'accès
@return : poids du répertoire contenant les textes. (devrait fonctionner pour les fichiers encodés mais aussi pour les fichiers initiaux.)
Chemin d'accès envisagé : input/    et input_compressed/
Etat de développement : fini, non testé
'''
    def get_dir_size(path='.'):
        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += get_dir_size(entry.path)
        return total
    
#    print(get_dir_size('input'))
#    print(get_dir_size('input_compressed'))
'''
@arguments : variable stockant le contenu sous format de chaîne de caractères, depuis un fichier txt
@return : dico = { 'caractère' : nb_occurences, ... }
Etat de développement : fini, non testé
'''
    def nb_ocurrences(txt):
        dico = {}
        for c in txt:
            if c in dico:
                dico[c]++
            else:
                dico[c] = 1
        return dico

'''
@arguments : chaine renvoyée par lire_txt()
@return : chaine_car_distincts
Etat de développement : fini, non testé
'''
    def car_distincts(chaine):
        myset = {}
        for c in chaine :
            myset.add(c)
        print(f"Nombre de caractères distincts dans la chaîne : "len(myset))
        
'''
@return : chaine_car_distincts
Etat de développement : non fini, non testé
'''
    def lire_txt()
        choix = input("Veuillez choisir parmi les oeuvres suivantes : ")
        for i in range contenu_dossier :
            print(f"{i} : {contenu_dossier[i]}")
            
        #switch:
        
