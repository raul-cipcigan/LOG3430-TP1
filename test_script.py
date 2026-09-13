from script import calculer_prix_final
import runpy

def test_montant_invalide():
    assert calculer_prix_final(0) == (
        "Erreur : Le montant doit etre strictement positif."
    )

def test_montant_1000():
    assert calculer_prix_final(1000) == (
        "Rabais applique (15%). Total a payer : 850.00 $"
    )

def test_montant_500():
    assert calculer_prix_final(500) == (
        "Rabais applique (10%). Total a payer : 450.00 $"
    )

def test_montant_100():
    assert calculer_prix_final(100) == (
        "Rabais applique (5%). Total a payer : 95.00 $"
    )

def test_montant_50():
    assert calculer_prix_final(50) == (
        "Aucun rabais applicable. Total a payer : 50.00 $"
    )

def test_script_argument_valide(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script.py", "50"])

    runpy.run_module("script", run_name="__main__")

    assert capsys.readouterr().out.strip() == (
        "Aucun rabais applicable. Total a payer : 50.00 $"
    )

def test_script_argument_invalide(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["script.py", "abc"])

    runpy.run_module("script", run_name="__main__")

    assert capsys.readouterr().out.strip() == (
        "Erreur : Veuillez fournir un nombre valide."
    )