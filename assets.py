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

# ==========================================================================
# === AFFICHAGE / COMPRESSION / SAUVEGARDE .csv ============================
# ==========================================================================

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


def compression(files,liste,input_dir,output_dir) :
    '''
    @arguments : files est une liste des noms de fichiers texte, liste est la liste des indices pour les fichiers sélectionnés
    et input_dir est le nom du dossier spécifié à l'exécution
    Fonction qui s'occupe de compresser tout les fichiers sélectionnés et de mettre les données relatives dans un fichier csv
    '''
    # SELECTION ENTIERE OU PARTIELLE DE FICHIERS
    if len(liste)!=0:   # Si l'utilisateur a fait une sélection, on sélectionne sur files les fichiers traités
        try:            # Sinon l'utilisateur sélectionne par défaut tout les fichiers
            files = [files[num] for num in liste]
        except IndexError:
            raise IndexError("Veuillez entrer des indices correspondant à ceux spécifiés.")

    # LECTURE DES FICHIERS
    for f in files:
        f_path = os.path.join(input_dir,f)
        with open(f_path,'r',encoding='utf-8') as file:
            
            if len(liste)==0:
                print(f"Fichier n°{files.index(f)} ./{input_dir}/{f} chargé.")
            else:
                print(f"Fichier n°{os.listdir(input_dir).index(f)} ./{input_dir}/{f} chargé.")
            
            # COMPRESSION
            texte = unidecode(file.read())
            arbre = NoeudHuffman.construire_huffman(texte)
            codes = arbre.encodage()
            compresse = arbre.compresser(texte, codes)
            
            # AFFICHAGE
            taille_initiale = len(texte) * 8
            taille_compressee = len(compresse)
            taux_compression = taux(taille_initiale,taille_compressee)
            print(f"Taille initiale     : {taille_initiale} bits")
            print(f"Taille compressée   : {taille_compressee} bits")
            print(f"Taux de compression : {taux_compression}%\n")
            
            # ENREGISTREMENT .CSV
            creation_csv("stats.csv")
            ecriture_csv("stats.csv",f,taille_initiale,taille_compressee,taux_compression)
            
            # SAUVEGARDE .HUFF
            nom_sortie = os.path.splitext(f)[0] + ".huff"
            chemin_sortie = os.path.join(output_dir, nom_sortie)
            sauvegarder_huff(chemin_sortie,output_dir,arbre,compresse)
            

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


# ==============================================================================
# === SAUVEGARDE COMPRESSION / CHARGEMENT .huff / DECOMPRESSION ================
# ==============================================================================
 
SEPARATEUR = "§".encode("utf-8")    # hors ASCII, donc jamais produit par unidecode()
                                    # ce qui en fait un bon séparateur (pas d'amalgame
                                    # avec les caractères encodés donc pas d'échappement)
 
def sauvegarder_huff(chemin_sortie,output_dir,arbre,bits):
    """
    @arguments: chemin_sortie est le chemin du fichier .huff à créer,
    arbre est l''arbre d'Huffman à sérialiser et bits est la chaîne de 0 et 1 produite
    par compresser()
    Sauvegarde un fichier .huff contenant :
      - l'arbre de Huffman sérialisé (header), c'est à dire qu'il est décrit linéairement
      - un séparateur '|'
      - le nombre de bits utiles du dernier octet (pour éviter le padding parasite)
      - un autre séparateur '|'
      - les données compressées en vrais octets binaires
    """
    arbre_ser = arbre.serialiser()
    
    # Cours utilisé: http://igm.univ-mlv.fr/~borie/cours/C_L3/L3C_cours7_4_on_1.pdf
    # On encode le fichier sur des octets, et écrire des bits de gauche à droite dans un fichier
    # peut causer un problème de décallage puisque le dernier octet peut ne pas être complet
    # donc on complète le dernier octet (padding) avec des 0. Aussi on spécifie en en-tête le nombre
    # de bits de padding pour la lecture.
    
    # Compléter la chaîne de bits pour qu'elle soit multiple de 8 (padding à droite avec des 0)
    padding = (8 - len(bits) % 8) % 8  # On utilise un deuxième %8 pour le cas suivant: (8-0)%8
                                       # autrement dit on ne veut pas de padding inutile (00000000)
    bits_paddes = bits + "0" * padding
    # bits_utiles = combien de bits du DERNIER octet sont réellement des données
    bits_utiles_dernier = 8 - padding if padding != 0 else 8
    
    # Convertir la chaîne de bits en vrais octets
    octets = bytearray()
    for i in range(0, len(bits_paddes), 8):
        octet = int(bits_paddes[i:i+8], 2) # Conversion int en base 2
        octets.append(octet)
    
    os.makedirs(output_dir, exist_ok=True)
    with open(chemin_sortie, "wb") as f:
        # Header : arbre sérialisé
        f.write(arbre_ser.encode("utf-8"))
        # Séparateur 1
        f.write(SEPARATEUR)
        # Nombre de bits utiles dans le dernier octet (stocké sur 1 octet, valeur 1-8)
        f.write(bytes([bits_utiles_dernier]))
        # Séparateur 2
        f.write(SEPARATEUR)
        # Données compressées
        f.write(octets)

 
def charger_huff(chemin_huff):
    """
    @arguments: chemin_huff est le chemin vers le fichier .huff
    @return: texte décompressé (str)
    Charge un fichier .huff et retourne le texte décompressé.
    """
    with open(chemin_huff, "rb") as f:
        contenu = f.read()
 
    parties = contenu.split(SEPARATEUR, 2)
    arbre_ser          = parties[0].decode("utf-8")
    bits_utiles_dernier = parties[1][0]
    octets             = parties[2]
 
    # Reconstruire la chaîne de bits
    bits = ""
    for j, octet in enumerate(octets):
        segment = format(octet, "08b") # Lecture par octet
        if j == len(octets) - 1:
            segment = segment[:bits_utiles_dernier]
        bits += segment
 
    # Reconstruire l'arbre
    arbre, _ = NoeudHuffman.deserialiser(arbre_ser)
 
    # Décompresser
    return arbre.decompresser(bits)

 
def decompression(chemin_huff,output_dir):
    """
    @arguments: chemin_huff est le chemin vers le fichier .huff à compresser,
    output_dir est le dossier où écrire le fichier texte décompressé
    Décompresse un fichier .huff et sauvegarde le résultat en .txt dans output_dir.
    """
    os.makedirs(output_dir, exist_ok=True) # Construit le dossier
                                           # et ne cause pas d'erreur si le dossier
                                           # existe déjà

    texte = charger_huff(chemin_huff)

    nom_base = os.path.splitext(os.path.basename(chemin_huff))[0]
    chemin_sortie = os.path.join(output_dir, nom_base + ".txt")

    with open(chemin_sortie, "w", encoding="utf-8") as f:
        f.write(texte)

    print(f"Fichier décompressé : {chemin_sortie}")
    return texte

