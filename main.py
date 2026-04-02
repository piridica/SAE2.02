# C5 - Samuel, Thenujan, Victor
# Fichier main.py
# importation des 3 modules authorisés dans le cadre de cette SAE2.02
from os import *
from sys import *
from unidecode import *
# importation des classes NoeudBinaire et NoeudHuffman
from NoeudBinaire import *  # permet de ne pas avoir à écrire nomFichier.nomFonction()...
from NoeudHuffman import *  # écriture plus concise.
# ==============================================================================

# Création d'un arbre binaire
racine = NoeudBinaire('A')
racine.set_gauche(NoeudBinaire('B'))
racine.set_droit(NoeudBinaire('C'))
racine.gauche.set_gauche(NoeudBinaire('D'))
racine.gauche.set_droit(NoeudBinaire('E'))
# [A[B[D[None,None],E[None,None]],C[None,None]]]
#         A
#        / \
#       B   C
#     / \
#    D   E

# Test des méthodes
print("Parcours préfixe (liste):", racine.parcours_prefixe())  # ['A', 'B', 'D', 'E', 'C']
print("Parcours préfixe (affichage):", end=' ')
racine.afficher_prefixe()  # Affiche: A B D E C




