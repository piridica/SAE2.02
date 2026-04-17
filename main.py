# C5 - Samuel, Thenujan, Victor
# Fichier main.py

# importation des 3 modules authorisés dans le cadre de cette SAE2.02
import os
import sys
#from unidecode import *     Utilisé sur assets.py

# importation des classes et des fichiers supplémentaires
from assets import *
#from NoeudBinaire import *  Utilisé sur assets.py
#from NoeudHuffman import *  Utilisé sur assets.py
#from tests import *         Ficher tests.py à exécuter seul

# ==============================================================================

if __name__ == "__main__":
    
    print("\n")
    print("="*40)
    print("=== COMPRESSION DE TEXTE PAR HUFFMAN " + "="*3)
    print("="*40 + "\n")

    # ENTREE A L'EXECUTION: NOM DE DOSSIER CONTENANT DES FICHIERS TEXTE
    try:
        input_dir = sys.argv[1]
        # On ne prend en compte que les fichiers texte
        files = [file for file in os.listdir(input_dir) if file.endswith('.txt')]
    except IndexError:
        raise IndexError("Il manque un paramètre: veuillez entrer le nom du fichier cible.")
    if len(files)==0:
        raise FileNotFoundError("Il n'y a pas de fichiers texte dans ce dossier.")
    
    # SELECTION DE FICHIERS POUR LA COMPRESSION
    print("Veuillez choisir le(s) texte(s) à compresser:\n")
    
    affiche_fichiers(files)
    
    print("\n-- entrez l'un des nombres")
    print("ou")
    print("-- entrez une plage (ex: (1,10))")
    print("ou")
    print("-- entrez une liste (ex: [1,5,6,10])")
    print("ou")
    print("-- sélectionnez tout par défaut")
    print("ou")
    print("-- entrez i pour accéder aux données de compression des fichiers compressés\n")
    
    choix_str = input(":").strip()
    
    if choix_str == "i":
        # DONNEES COMPRESSION
        print("\n")
        afficher_csv("stats.csv")
    else:
        # COMPRESSION
        print("\n")
        choix = listage(choix_str)
        compresse = compression(files,choix,input_dir)

