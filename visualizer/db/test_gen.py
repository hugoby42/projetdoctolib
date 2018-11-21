import pytest
import visualizer.db.gen as gen

def test_formalise_nom():
    #on renvoie un string
    assert(gen.formalise_nom(1) == '1')
    #on enlève les espaces
    assert(gen.formalise_nom(' Toulouse   ') == 'Toulouse')
    #On a le format demandé
    assert(gen.formalise_nom('TOULOUSE') == 'Toulouse')

test_formalise_nom()

def test_combien_fichier():
    #on renvoie une liste
    assert(type(gen.combien_fichier(1,'12/09/2018',40))==list)
test_combien_fichier()

def test_As_tu_copier():
    #si il n'y a qu'un candidat on a une liste vide
    assert(gen.As_tu_copier(0,1) == [])
    #on renvoie une liste
    assert(type(gen.As_tu_copier(1,40)) == list)
test_As_tu_copier()

def test_creation_candidat():
    #on renvoie un dictionnaire
    assert(type(gen.creation_candidat(0,40)) == dict)
test_creation_candidat()

def test_creation_n_candidats():
    #on renvoie une liste
    assert(type(gen.creation_n_candidats(40)) == list)
    #la liste a une longueur n
    assert(len(gen.creation_n_candidats(40)) == 40)
    #chaque élément de la liste est un dictionnaire
    assert(type(gen.creation_n_candidats(40)[0]) == dict)
test_creation_n_candidats()
