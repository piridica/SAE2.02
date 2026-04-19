# C5 - Samuel, Thenujan, Victor
# Fichier assets.py
# ___________________________________________
# Contient des fonctions utiles pour le main:
# - pour la compression
# - pour le traitement de fichier csv

# Imports autorisés
import os
from unidecode import *

# Imports des classes
from NoeudHuffman import *
# from NoeudBinaire import *  Non utile


def affiche_fichiers(files) :
    '''
    @arguments : files est une liste de nom de fichiers
    Fonction permettant d'afficher les noms des fichiers texte contenus dans le répertoire spécifié
    '''
    for f in files:
        if f.endswith('.txt'):
            print(f"{files.index(f)}.{f}")


def listage(choix_str):
    '''
    @arguments: choix_str est la chaîne de caractère venant de l'entrée utilisateur pour la sélection de fichiers
    @return : liste des indices des fichiers sélectionnés
    Fonction qui convertit l'entrée utilisateur de la sélection en une liste
    '''
    try:
        if choix_str.startswith("["):
            choix = list(map(int, choix_str[1:-1].split(",")))
        elif choix_str.startswith("("):
            a,b = tuple(map(int, choix_str[1:-1].split(",")))
            choix = [i for i in range(a,b+1)]
        elif len(choix_str)!=0:
            choix = [int(choix_str)]
        else:
            choix = []
    except ValueError:
        raise ValueError("Veuillez entrer le bon format pour la sélection des fichiers.")
    return choix
    

def taux(taille_initiale,taille_compressee) :
    '''
    @arguments : taille en bits du fichier initial et celui du fichier encodé
    @return : taux de compression en pourcentage
    Fonction qui donne le taux de compression en pourcentage sur la taille du fichier
    '''
    return round((1 - taille_compressee / taille_initiale) * 100, 2)


def compression(files,liste,input_dir) :
    '''
    @arguments : files est une liste des noms de fichiers texte, liste est la liste des indices pour les fichiers sélectionnés
    et input_dir est le nom du dossier spécifié à l'exécution
    Fonction qui s'occupe de compresser tout les fichiers sélectionnés et de mettre les données relatives dans un fichier csv
    '''
    if len(liste)!=0:   # Si l'utilisateur a fait une sélection, on sélectionne sur files les fichiers traités
        try:            # Sinon l'utilisateur sélectionne par défaut tout les fichiers
            files = [files[num] for num in liste]
        except IndexError:
            raise IndexError("Veuillez entrer des indices correspondant à ceux spécifiés.")
    for f in files:
        f_path = os.path.join(input_dir,f)
        with open(f_path,'r',encoding='utf-8') as file:
            if len(liste)==0:
                print(f"Fichier n°{files.index(f)} ./{input_dir}/{f} chargé.")
            else:
                print(f"Fichier n°{os.listdir(input_dir).index(f)} ./{input_dir}/{f} chargé.")
            texte = unidecode(file.read())
            arbre = NoeudHuffman.construire_huffman(texte)
            codes = arbre.encodage()
            compresse = arbre.compresser(texte, codes)
            taille_initiale = len(texte) * 8
            taille_compressee = len(compresse)
            taux_compression = taux(taille_initiale,taille_compressee)
            print(f"Taille initiale     : {taille_initiale} bits")
            print(f"Taille compressée   : {taille_compressee} bits")
            print(f"Taux de compression : {taux_compression}%\n")
            creation_csv("stats.csv")
            ecriture_csv("stats.csv",f,taille_initiale,taille_compressee,taux_compression)
            

def ecriture_csv(chemin_csv,nom_fichier,ti,tc,taux):
    '''
    Fonction qui vérifie s'il y a déjà bien les informations de compression d'un fichier sur le csv
    pour éviter les doublons, autrement il rajoute à la suite les données: nom du fichier,
    la taille initiale, la taille après compression et le taux de compression
    '''
    existe = donnees_existantes(chemin_csv)
    if nom_fichier not in existe:
        ajouter_csv(chemin_csv,nom_fichier,ti,tc,taux)


def donnees_existantes(chemin_csv):
    '''
    Fonction qui renvoie une liste des nom de fichiers qui sont déjà mentionnés dans le csv afin de pouvoir 
    éviter les doublons par la suite
    '''
    if not os.path.exists(chemin_csv):
        return []
    existe = []
    with open(chemin_csv,"r",encoding="utf-8") as f:
        next(f,None) # Ignorer le header (les champs du csv)
        for ligne in f:
            existe.append(ligne.strip().split(",")[0])
    return existe


def ajouter_csv(chemin_csv,nom_fichier,ti,tc,taux):
    '''
    Fonction qui rajoute une ligne d'info sur un fichier compressé (sachant qu'il n'y a pas de doublon)
    '''
    with open(chemin_csv,"a",encoding="utf-8") as f:
        f.write(f"{nom_fichier},{ti},{tc},{taux}\n")


def creation_csv(chemin_csv):
    '''
    Fonction de création du csv
    '''
    if not os.path.exists(chemin_csv) or os.path.getsize(chemin_csv) == 0:
        with open(chemin_csv, "w", encoding="utf-8") as f:
            f.write("nom_fichier,taille_initiale,taille_compressee,taux_compression\n")


def afficher_csv(chemin_csv):
    if not os.path.exists(chemin_csv):
        print("Aucune donnée à afficher.")
        return
    with open(chemin_csv, "r", encoding="utf-8") as f:
        next(f, None)
        lignes = [ligne.strip().split(",") for ligne in f]
    if not lignes:
        print("Aucune donnée à afficher.")
        return

    # Calcul dynamique des largeurs selon le contenu
    largeur_nom  = max(len(l[0]) for l in lignes) + 2
    largeur_ti   = max(len(l[1]) for l in lignes) + 2
    largeur_tc   = max(len(l[2]) for l in lignes) + 2
    largeur_taux = max(len(l[3]) for l in lignes) + 2

    # On s'assure que les headers rentrent aussi
    largeur_nom  = max(largeur_nom,  len("FICHIER")     + 2)
    largeur_ti   = max(largeur_ti,   len("TAILLE_INIT") + 2)
    largeur_tc   = max(largeur_tc,   len("TAILLE_COMP") + 2)
    largeur_taux = max(largeur_taux, len("TAUX")        + 2)

    sep = largeur_nom + largeur_ti + largeur_tc + largeur_taux
    print(f"{'FICHIER':<{largeur_nom}} {'TAILLE_INIT':<{largeur_ti}} {'TAILLE_COMP':<{largeur_tc}} {'TAUX':<{largeur_taux}}")
    print("-" * sep)
    for nom, ti, tc, taux in lignes:
        print(f"{nom:<{largeur_nom}} {ti:<{largeur_ti}} {tc:<{largeur_tc}} {taux+"%":<{largeur_taux}}")

    print()


