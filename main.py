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
 
USAGE = """
Usage :
  python main.py -c <dossier>   Compresser les .txt du dossier
  python main.py -d <dossier>   Décompresser un .huff du dossier output/
  python main.py -i             Afficher les statistiques de compression
"""
 
USAGE2 = """
-- un indice        ex: 1
-- une plage        ex: (0,2)
-- une liste        ex: [0,2,4]
-- entrée vide      tous les fichiers
"""
def erreur(message):
    print(USAGE)
    print(f"main.py: {message}")
    sys.exit(1)
 
# ==============================================================================
 
if __name__ == "__main__":

    # --- LECTURE DES ARGUMENTS -------------------------------------------
    if len(sys.argv) < 2:
        erreur("nombre d'arguments incorrect.")
 
    flag = sys.argv[1]   # -c, -d ou -i
 
    if flag not in ("-c", "-d", "-i"):
        erreur(f"flag '{flag}' inconnu.")
    
    # Affichage des informations des fichiers précédemment compressés
    if flag == "-i":
        afficher_csv("stats.csv")
        sys.exit(0)
 
    if flag in ("-c", "-d") and len(sys.argv) < 3:
        erreur("nombre d'arguments incorrect.")
 
    if flag in ("-c", "-d"):
        input_dir  = sys.argv[2]   # dossier source
        output_dir = sys.argv[3] if len(sys.argv) == 4 else ("compresse" if flag == "-c" else "decompresse")   # dossier de sortie
 
        if not os.path.exists(input_dir):
            erreur(f"le dossier '{input_dir}' n'existe pas.")
 
    # --- COMPRESSION ------------------------------------------------------
    if flag == "-c":
 
        # On ne prend en compte que les fichiers texte
        files_txt = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
        if len(files_txt) == 0:
            raise FileNotFoundError(f"Aucun fichier .txt trouvé dans '{input_dir}'.")
 
        # SELECTION DE FICHIERS POUR LA COMPRESSION
        print("\nVeuillez choisir le(s) texte(s) à compresser :\n")
        affiche_fichiers(files_txt)
        print(USAGE2)
 
        choix_str = input(": ").strip()
        print()
        liste = listage(choix_str)
        compression(files_txt, liste, input_dir, output_dir)
 
    # --- DECOMPRESSION ---------------------------------------------------
    elif flag == "-d":

        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Aucun dossier {input_dir} trouvé. Compressez d'abord un fichier.")
 
        # On ne prend en compte que les fichiers .huff
        files_huff = [f for f in os.listdir(input_dir) if f.endswith('.huff')]
        if len(files_huff) == 0:
            raise FileNotFoundError(f"Aucun fichier .huff trouvé dans {input_dir}.")

        # SELECTION DE FICHIERS POUR LA DECOMPRESSION
        print("\nVeuillez choisir le(s) fichier(s) à décompresser :\n")
        for i, f in enumerate(files_huff):
            print(f"  {i}. {f}")
        print(USAGE2)
 
        choix_str = input(": ").strip()
        print()
        liste = listage(choix_str)
 
        if len(liste) != 0:
            try:
                files_huff = [files_huff[i] for i in liste]
            except IndexError:
                raise IndexError("Veuillez entrer des indices correspondant à ceux spécifiés.")
        
        for fichier_huff in files_huff:
            chemin_huff = os.path.join(input_dir, fichier_huff)
            decompression(chemin_huff, output_dir)

