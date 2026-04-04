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

print("\n" + "="*60)
print("Tests NoeudBinaire :")
print("="*60)
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


# ==============================================================================
#Tests pour le fichier NoeudHuffman

#Proposition de chaine de caractere a essaye pour le test
chaine = "Comment ca va ?"

#Affichage de la separation
print("\n" + "="*60)
print("Tests NoeudHuffman sur la chaîne :", chaine)
print("="*60)

# Construction de l'arbre
arbre = NoeudHuffman.depuis_chaine(chaine)
print("\nArbre de Huffman :")
print(arbre)

# Encodage
codes = arbre.encodage()
print("\nEncodage des caractères :")
for caractere, code in sorted(codes.items(), key=lambda x: x[1]):
    print(f"  '{caractere}' -> {code}")

# Compression
compresse = arbre.compresser(chaine, codes)
taille_initiale = len(chaine) * 8
taille_compressee = len(compresse)
print(f"\nChaîne originale    : {chaine}")
print(f"Chaîne compressée   : {compresse}")
print(f"Taille initiale     : {taille_initiale} bits")
print(f"Taille compressée   : {taille_compressee} bits")
print(f"Taux de compression : {round((1 - taille_compressee / taille_initiale) * 100, 2)}%")

# Decompression
decompresse = arbre.decompresser(compresse)
print(f"\nChaîne décompressée : {decompresse}")
if decompresse == chaine:
    print("Décompression correspond à l'original.")
else:
    print("ERREUR - la décompression ne correspond pas à l'original.")
