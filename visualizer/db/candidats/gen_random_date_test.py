import pytest
import visualizer.db.candidats.gen_random_date as grd

def test_date_aleatoire_entre_start_end():
    assert type(grd.date_aleatoire_entre_start_end()) == str

def test_dates_aleatoires_naissance_entretien():
    assert type(grd.dates_aleatoires_naissance_entretien()) == list

def test_date_depot_fichier():
    assert type(grd.date_depot_fichier()) == str
    dates = []
    for k in range (31):
        dates.append([str(k)+"/09/2018"])
    for date_entretien in dates:
        assert grd.date_depot_fichier(date_entretien) >= date_entretien
