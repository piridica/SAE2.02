# C5 - Samuel, Thenujan, Victor
# Fichier main.py

# importation des 3 modules authorisés dans le cadre de cette SAE2.02
#from os import *
#from sys import *
#from unidecode import *

# importation des classes
from NoeudBinaire import * 
from NoeudHuffman import *

# ==============================================================================
# === TESTS: NOEUDBINAIRE ======================================================
# ==============================================================================


# --- DEFINITIONS D'ARBRES -----------------------------------------------------

def ex_arbrebinaire1():
  g = NoeudBinaire('G', None, None) # Arbre de valeur 'G', sans sous-arbre (feuille)
  # Arbre de valeur 'F'. Sous-arbre gauche : g. Pas sous-arbre droit.
  f = NoeudBinaire('F', g, None)
  # Arbre de valeur 'E'. Pas de sous-arbre gauche. Sous-arbre droit : f
  e = NoeudBinaire('E', None, f)
  d = NoeudBinaire('D', None, None) # Arbre de valeur 'D', sans sous-arbres (feuille)
  c = NoeudBinaire('C', None, None) # Arbre de valeur 'C', sans sous-arbres (feuille)
  # Arbre de valeur 'B', sous-arbre gauche : c. Sous-arbre droit : d.
  b = NoeudBinaire('B', c, d)
  # Arbre de valeur 'A', sous-arbre gauche : b. Sous-arbre droit : e.
  a = NoeudBinaire('A', b, e)
  return a
  #
  #         A
  #      /     \
  #     B       E
  #    / \     / \
  #   C   D       F
  #              / \
  #           G

def ex_arbrebinaire2():
  c = NoeudBinaire('C', None, None)
  a = NoeudBinaire('A', None, c)
  return a
  #
  #       A
  #      / \
  #         C

def ex_racine():
  return NoeudBinaire('A', None, None)
  #
  #       A
  #      / \

def ex_arbrevide():
  return NoeudBinaire(None, None, None)
  #
  #     (vide)

# --- TESTS DES METHODES -------------------------------------------------------

def test_est_vide():
  assert(ex_arbrebinaire1().est_vide()==False)
  assert(ex_arbrebinaire2().est_vide()==False)
  assert(ex_racine().est_vide()==False)
  assert(ex_arbrevide().est_vide()==True)

def test_est_feuille():
  assert(ex_arbrebinaire1().est_feuille()==False)
  assert(ex_arbrebinaire2().est_feuille()==False)
  assert(ex_racine().est_feuille()==True)
  assert(ex_arbrevide().est_feuille()==False)

def test_a_gauche():
  assert(ex_arbrebinaire1().a_gauche()==True)
  assert(ex_arbrebinaire2().a_gauche()==False)
  assert(ex_racine().a_gauche()==False)
  assert(ex_arbrevide().a_gauche()==False)

def test_a_droite():
  assert(ex_arbrebinaire1().a_droite()==True)
  assert(ex_arbrebinaire2().a_droite()==True)
  assert(ex_racine().a_droite()==False)
  assert(ex_arbrevide().a_droite()==False)

def test_hauteur():
  assert(ex_arbrebinaire1().hauteur()==4)
  assert(ex_arbrebinaire2().hauteur()==2)
  assert(ex_racine().hauteur()==1)
  assert(ex_arbrevide().hauteur()==0)

def test_str():
  '''
  Test de comparaison visuelle entre les affichages d'arbres et les arbres écrits en commentaire plus haut
  '''
  print("TEST VISUEL: méthode __str__ de NoeudBinaire")
  print("-- Veuillez vérifier que les arbres affichés")
  print("-- correspondent à ceux dessinés dans le code. \n")
  
  print("- cas d'un arbre binaire non vide, de hauteur supérieure à 2 \n")
  print(ex_arbrebinaire1())
  
  print("- cas d'un arbre non vide, de hauteur égale à 2 \n")
  print(ex_arbrebinaire2())
  
  print("- cas d'un arbre non vide, de hauteur égale à 1 \n")
  print(ex_racine())
  
  print("- cas d'un arbre vide \n")
  print(ex_arbrevide())

def test_parcours_prefixe():
  a = ex_arbrebinaire1()
  attendu = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  assert a.parcours_prefixe() == attendu

def test_parcours_infixe():
  a = ex_arbrebinaire1()
  attendu = ['C', 'B', 'D', 'A', 'E', 'G', 'F']
  assert a.parcours_infixe() == attendu

def test_parcours_suffixe():
  a = ex_arbrebinaire1()
  attendu = ['C', 'D', 'B', 'G', 'F', 'E', 'A']
  assert a.parcours_suffixe() == attendu

def test_parcours_largeur():
  a = ex_arbrebinaire1()
  attendu = ['A', 'B', 'E', 'C', 'D', 'F', 'G']
  assert a.parcours_largeur() == attendu

# --- TESTS DES GETTERS,SETTERS ------------------------------------------------

def test_get_valeur():
  '''
  Teste l'obtention de la valeur de la racine
  '''
  assert(ex_arbrebinaire1().get_valeur()=='A')
  assert(ex_arbrebinaire2().get_valeur()=='A')
  assert(ex_racine().get_valeur()=='A')
  assert(ex_arbrevide().get_valeur()==None)
  
def test_set_valeur():
  '''
  Teste la modification de la valeur de la racine
  '''
  # Il est interdit de rendre la racine vide car il y a au moins un sous-arbre
  for a in (ex_arbrebinaire1(),ex_arbrebinaire2()): # (Ces arbres ont au moins un sous-arbre)
    # On peut modifier la racine
    a.set_valeur('M')
    assert(a.get_valeur()=='M')
    # On ne doit pas réussir à vider la racine
    try:
      a.set_valeur(None)
      assert False
    except ValueError: # Si set_valeur provoque une erreur alors le cas limite est bien traité
      pass
  # Ici il n'y a pas de sous-arbres donc on peut rendre la racine vide
  for a in (ex_racine(),ex_arbrevide()): # (Ces arbres n'ont pas de sous-arbre)
    # On peut modifier la racine
    a.set_valeur('M')
    assert(a.get_valeur()=='M')
    # On peut rendre la racine vide
    a.set_valeur(None)
    assert(a.get_valeur()==None)
  
def test_get_gauche():
  '''
  Teste l'obtention du sous-arbre gauche
  '''
  # On peut se satisfaire de tester pour arbrebinaire1
  a = ex_arbrebinaire1()
  b = a.get_gauche()
  assert(b.get_valeur()=='B')
  c = b.get_gauche()
  assert(c.get_valeur()=='C')
  rien = c.get_gauche()
  assert rien is None
  
def test_set_gauche():
  '''
  Teste la modification du sous-arbre gauche
  '''
  # Il est interdit de rendre le sous-arbre gauche non vide si la racine est vide
  a = ex_arbrevide()
  b = ex_racine()
  try:
    # On ne doit pas pouvoir réussir à rendre le sous-arbre gauche vide si la racine est vide
    a.set_gauche(b)
    assert False
  except ValueError: # Si set_gauche provoque une erreur alors on a bien traité le cas limite
    pass
  # Dans le cas où la racine n'est pas vide, on peut agir comme il nous semble sur le sous-arbre gauche
  # On peut le modifier
  a = ex_racine()
  b = ex_racine()
  a.set_gauche(b)
  assert a.get_gauche() == b
  # On peut le rendre vide
  b = ex_arbrevide()
  a.set_gauche(b)
  assert a.get_gauche() == b
  
  
def test_get_droite():
  '''
  Teste l'obtention du sous-arbre droit
  '''
  # Il est à nouveau suffisant de tester pour arbrebinaire1
  a = ex_arbrebinaire1()
  e = a.get_droite()
  assert(e.get_valeur()=='E')
  f = e.get_droite()
  assert(f.get_valeur()=='F')
  rien = f.get_droite()
  assert rien is None
  
def test_set_droite():
  '''
  Teste la modification du sous-arbre droit
  '''
  # Il est interdit de rendre le sous-arbre droit non vide si la racine est vide
  a = ex_arbrevide()
  b = ex_racine()
  try:
    # On ne doit pas pouvoir réussir à rendre le sous-arbre droit vide si la racine est vide
    a.set_droite(b)
    assert False
  except ValueError: # Si set_droite provoque une erreur alors on a bien traité le cas limite
    pass
  # Dans le cas où la racine n'est pas vide, on peut agir comme il nous semble sur le sous-arbre droit
  # On peut le modifier
  a = ex_racine()
  b = ex_racine()
  a.set_droite(b)
  assert a.get_droite() == b
  # On peut le rendre vide
  b = ex_arbrevide()
  a.set_droite(b)
  assert a.get_droite() == b

# ==============================================================================
# === TESTS: NOEUDHUFFMAN ======================================================
# ==============================================================================





# ==============================================================================
# === MAIN =====================================================================
# ==============================================================================

def test_noeudbinaire():
  '''
  Teste la classe NoeudBinaire
  '''
  print("\n")
  print("Tests NoeudBinaire ... \n")
  # METHODES
  test_est_vide()
  test_est_feuille()
  test_a_gauche()
  test_a_droite()
  test_hauteur()
  test_str()
  test_parcours_prefixe()
  test_parcours_infixe()
  test_parcours_suffixe()
  test_parcours_largeur()
  # GETTERS, SETTERS
  test_get_valeur()
  test_set_valeur()
  test_get_gauche()
  test_set_gauche()
  test_get_droite()
  test_set_droite()
  print("OK")

def test_noeudhuffman():
  #print("Tests NoeudHuffman ...")
  
  #print("OK")

# ==============================================================================

if __name__ == "__main__":
  test_noeudbinaire()
  #test_noeudhuffman()

