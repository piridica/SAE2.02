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

# Création d'un arbre binaire exemple :
racine = NoeudBinaire('A')
racine.set_gauche(NoeudBinaire('B'))
racine.set_droite(NoeudBinaire('C'))
racine.gauche.set_gauche(NoeudBinaire('D'))
racine.gauche.set_droite(NoeudBinaire('E'))
# [A[B[D[None,None],E[None,None]],C[None,None]]]
#         A
#        / \
#       B   C
#     / \
#    D   E

# Test des méthodes
# Préfixe
print("Parcours préfixe (liste):", racine.parcours_prefixe())  # ['A', 'B', 'D', 'E', 'C']
print("Parcours préfixe (affichage):", end=' ')
racine.afficher_prefixe()  # Affiche: A B D E C

# Suffixe
# racine.afficher_suffixe()

# Infixe
# racine.afficher_suffixe()

# Parcours en largeur
# racine.afficher_largeur()



