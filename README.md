# Compression de Texte par encodage d'Huffman
> SAE 2.02 — Exploration algorithmique d'un problème  
> BUT 1 Informatique — Groupe C5

**Samuel MIHAILA · Victor BUGA · Thenujan NANTHAKUMAR**

---

## Structure du projet

```
projet-huffman/
│
├── main.py              # Point d'entrée du programme
├── NoeudBinaire.py      # Classe de base : arbre binaire générique
├── NoeudHuffman.py      # Classe héritée : arbre de Huffman
├── assets.py            # Fonctions utilitaires (compression, CSV)
├── test.py              # Tests unitaires et visuels
│
├── <stats.csv>          # Généré automatiquement — statistiques de compression
└── <dossier_input>/     # Dossier contenant les fichiers .txt à compresser
```

---

## Prérequis

```bash
pip install unidecode
```

---

## Utilisation

```bash
python main.py <paramètre> <nom_dossier_entree> [nom_dossier_destination]
```

Paramètres:
-i:  affichage des informations de compression enregistrés dans stats.csv
-c:  compression de fichiers .txt en fichiers .huff
-d:  décompression de fichiers .huff en fichiers .txt

**Exemple :**

```bash
python main.py -c input
```

### Sélection des fichiers

Au lancement avec '-c', le programme affiche la liste des fichiers `.txt` disponibles :

```
0. leCid.txt
1. lesMiserables.txt
2. marcheTrain.txt
```

| Entrée | Comportement |
|--------|-------------|
| `1` | Compresse uniquement le fichier n°1 |
| `[0,2]` | Compresse les fichiers n°0 et n°2 |
| `(0,2)` | Compresse les fichiers n°0 à n°2 (plage inclusive) |
| *(vide)* | Compresse **tous** les fichiers du dossier |
| `i` | Affiche les statistiques de compression enregistrées |

---

## Statistiques de compression

Les résultats sont automatiquement sauvegardés dans `stats.csv` et consultables via l'option `-i` :

```
FICHIER                TAILLE_INIT   TAILLE_COMP   TAUX
------------------------------------------------------
leCid.txt              45231040      24876512      44.97%
lesMiserables.txt      12083200      6601344       45.36%
marcheTrain.txt        8941600       4897344       45.22%
```

---

## Tests

Exécuter le fichier de tests indépendamment :

```bash
python test.py
```

Les tests couvrent :
- Toutes les méthodes de `NoeudBinaire` (getters, setters, parcours, structure)
- La construction de l'arbre de Huffman
- L'encodage, la compression et la décompression
- Vérification que `decompresser(compresser(chaine)) == chaine`
