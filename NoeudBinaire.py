# C5 - Samuel, Thenujan, Victor
# Fichier NoeudBinaire.py

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
            if self.gauche != None or self.droit != None :  # vérifie si l'un des sous-arbres n'est pas vide
                raise ExpectionError("Vous ne pouvez pas supprimer un noeud ayant des sous-noeuds!")
        else :
            self.valeur = valeur  # mise à jour du noeud
    
    # gauche
    def get_gauche( self ) :
        return self.gauche
    def set_gauche( self, gauche ) :
        self.gauche = gauche
    
    # droit
    def get_droit( self ) :
        return self.droit
    def set_droit( self, droit ) :
        self.droit = droit
    
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
    '''
    @arguments : poids du fichier initial, puis celui du fichier encodé
    @return : taux de compression en %
    Etat de développement : fini, non testé
    '''
    def taux_compression( mem_txt, mem_txt_encode ) :
        return ((
                        mem_txt - mem_txt_encode) / mem_txt) * 100  # à voir s'il vaut mieux conserver le *100 ou pas. les deux se vallent
    
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
    
    """
    @arguments : directory est un chemin d'accès vers un répertoire.
    Méthode permettant d'afficher une liste des fichiers contenus dans un répértoire.
    """
    def affiche_fichiers( directory ) :
        # Liste seulement les fichiers en excluant les sous-répertoires
        files = [ f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) ]
        # affichage de l'ensemble des fichiers situés dans le dossier
        print("Veuillez choisir parmi les oeuvres suivantes : ")
        for i, file in enumerate(files, start = 1) :
            print(f"{i} : {file}")
    
    '''
    @arguments : chemin d'accès
    @return : poids du répertoire contenant les textes. (devrait fonctionner pour les fichiers encodés mais aussi pour les fichiers initiaux.)
    Chemin d'accès envisagé : input/    et input_compressed/
    Etat de développement : fini, non testé
    '''
    def get_dir_size( "." ) :
        total = 0
        with os.scandir(path) as it :
            for entry in it :
                if entry.is_file() :
                    total += entry.stat().st_size
                elif entry.is_dir() :
                    total += get_dir_size(entry.path)
        return total
    
    #    print(get_dir_size('/input'))
    #    print(get_dir_size('/input_compressed'))
    '''
    @arguments : variable stockant le contenu sous format de chaîne de caractères, depuis un fichier txt
    @return : dico = { 'caractère' : nb_occurences, ... }
    Etat de développement : fini, non testé
    '''
    def nb_ocurrences( txt ) :
        dico = {}
        for c in txt :
            if c in dico :
                dico[ c ] += 1
            else :
                dico[ c ] = 1
        return dico
    
    '''
    car_distincts()     Approche de Victor, à remplacer éventuellement en faveur de l'approche nb_occurrences() avec une conversion
                        list(dico.keys()). Cette approche (Samuel) permet de conserver le nombre d'ocurrences des caractères.
    @arguments : chaine renvoyée par lire_txt()
    @return : chaine_car_distincts
    Etat de développement : fini, non testé
    '''
    def car_distincts( chaine ) :
        myset = {}
        for c in chaine :
            myset.add(c)
        print(f"Nombre de caractères distincts dans la chaîne : ", len(myset))
        
        '''
    choix_dossier() correspond à une boucle imbriquée dans la fonction lire_txt()
    @return directory qui correspond au chemin d'accès du dossier contenant les oeuvres au format ASCII, brut, et encodées.
    Etat de développement : fini, non testé
    '''
    def choix_dossier() :
        while continuer_bis :  # boucle responsable du choix du dossier : compressé ou brut
            choix_dossier = input("Souhaitez vous lire : \n1 : les fichiers compressés \n 2 : les fichiers bruts?")
            if choix_dossier == 1 :  # fichiers bruts
                directory = "/input"  # affectation du chemin d'accès menant vers le répertoire contenant les fichiers bruts
                continuer_bis = False  # la boucle s'interrompt
                return directory
            elif choix_dossier == 2 :  # fichiers compressés
                directory = "/input_compressed"  # affectation du chemin d'accès menant vers le répertoire contenant les fichiers compressés
                continuer_bis = False  # la boucle s'interrompt
                return directory
            else :
                print("Veuillez réinsérer une valeur valide.")
                continuer_bis = True  # la boucle poursuit
    
    '''
    lire_txt() s'adapte au contenu brut et compressé.
    @return : contenu du fichier séléctionné
    Etat de développement : fini, non testé
    '''
    def lire_txt() :
        content = ""  # Déclaration/Initialisation du contenu extrait du fichier.txt, initialement vide. (str)
        continuer = True  # condition d'arrêt de la première boucle, intégrant la totalité de la fonction
        continuer_bis = True  # condition d'arrêt de la boucle imbriquée, responsable du choix du dossier par l'utilisateur
        directory = ""  # Affectation du chemin d'accès du répertoire comme chaîne de caractères vide.
        
        while continuer :
            directory = choix_dossier()  # appel de la fonction permettant de choisir entre dossier brut et dossier encodé
            affiche_fichiers(
                directory)  # appel de procédure permettant d'afficher l'ensemble des fichiers du dossier séléctionné
            
            choix = input("Votre choix : ")
            try :
                choix_int = int(choix) - 1  # Convertir en index (0-based)
                if 0 <= choix_int < len(
                        files) :  # Vérification que l'utiulisateur n'a pas inséré une valeur supérieure au nombre de fichiers
                    print(f"Vous avez choisi {files[ choix_int ]}")  # Affichage du fichier séléctionné dans la console
                    with open(os.path.join(directory, files[ choix_int ]),
                              'r') as f :  # ouvre le fichier en mode lecture
                        content = f.read()  # affecte le contenu du fichier à la variable content. format str
                    continuer = False  # interruption de la boucle principale
                
                else :  # le choix de l'utilisateur n'est pas valide, cas de marge
                    print("Votre choix est en dehors de la plage valide. Veuillez réessayer.")
            
            except ValueError :  # l'input de l'utilisateur est impossible à interpréter
                print("Veuillez entrer un nombre valide.")
        
        return content  # renvoie le contenu extrait de l'oeuvre choisie par l'utilisateur.
