# C5 - Samuel, Thenujan, Victor
# Fichier main.py
# importation des 3 modules authorisés dans le cadre de cette SAE2.02
from os import *
from sys import *
from unidecode import *

# importation des classes NoeudBinaire et NoeudHuffman
from NoeudBinaire import *  # permet de ne pas avoir à écrire nomFichier.nomFonction()...
from NoeudHuffman import *  # écriture plus concise.
# importation d'outils supplémentaires ne relevant des classes NoeudBinaire et NoeudHuffman : fonctions / méthodes
from Assets import *
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

# ------------------------------------------------------------------------------

# Test des méthodes
print("Tests :")
# Préfixe - Validé
print("Parcours préfixe (liste):", racine.parcours_prefixe())  # ['A', 'B', 'D', 'E', 'C']
print("Parcours préfixe (affichage):", end=' ')
racine.afficher_prefixe()  # Affiche: A B D E C

# Suffixe - à valider

print("\n\nParcours suffixe (liste):", racine.parcours_suffixe())  # ['D', 'E', 'B', 'C', 'A']
print("Parcours suffixe (affichage):", end=' ')
racine.afficher_suffixe()  # Affiche: D E B C A

# Infixe - Validé
print("\n\nParcours infixe (liste):", racine.parcours_infixe())  # ['D', 'B', 'E', 'A', 'C']
print("Parcours infixe (affichage):", end=' ')
racine.afficher_infixe()  # Affiche: D B E A C

# Parcours en largeur

print("\n\nParcours en largeur (liste):", racine.parcours_largeur())  # ['A', 'B', 'C', 'D', 'E']
print("Parcours en largeur (affichage):", end=' ')
racine.afficher_largeur()  # Affiche: A B C D E

# ------------------------------------------------------------------------------


