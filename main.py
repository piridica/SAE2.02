# C5 - Samuel, Thenujan, Victor
# Fichier main.py

# importation des 3 modules authorisés dans le cadre de cette SAE2.02
from os import *
from sys import *
from unidecode import *

# importation des classes et des fichiers supplémentaires
from NoeudBinaire import * 
from NoeudHuffman import *
from Assets import *
from tests import *

# ==============================================================================

if __name__ == "__main__":

    print("\n")
    print("="*42)
    print("=== COMPRESSION DE TEXTE SELON HUFFMAN " + "="*3)
    print("="*42 + "\n")

    # Enregistrement de l'entrée en cli (dossier cible)
    try:
        input_dir = sys.argv[1]
    except IndexError:
        raise IndexError("Il manque un paramètre: veuillez entrer le nom du fichier cible.")
    if len(os.listdir(input_dir))==0:
        raise FileNotFoundError("Il n'y a pas de fichiers dans ce dossier.")
    
    # Sélection de fichiers pour la compression
    print("Veuillez choisir le(s) texte(s) à compresser:\n")
    affiche_fichiers(input_dir)
    print("\n-- entrez l'un des nombres")
    print("ou")
    print("-- entrez une plage (ex: (1,10))")
    print("ou")
    print("-- entrez une liste (ex: [1,5,6,10])")
    print("ou")
    print("-- sélectionnez tout par défaut\n")
    choix_str = input(":").strip()
    choix = listage(choix_str)
    
    # Lecture des fichiers
    fichiers = 
    textes = lire_txt(fichier,liste)

