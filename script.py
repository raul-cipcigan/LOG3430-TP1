import sys

def calculer_prix_final(montant):
    if montant <= 0:
        return "Erreur : Le montant doit etre strictement positif."

    rabais = 0
    if montant >= 1000:
        rabais = 15
    elif montant >= 500:
        rabais = 10
    elif montant >= 100:
        rabais = 5

    if rabais > 0:
        prix_escompte = montant * (1 - rabais / 100)
        return f"Rabais applique ({rabais}%). Total a payer : {prix_escompte:.2f} $"
    else:
        return f"Aucun rabais applicable. Total a payer : {montant:.2f} $"

if __name__ == "__main__":
    try:
        valeur = float(sys.argv[1])
        print(calculer_prix_final(valeur))
    except ValueError:
        print("Erreur : Veuillez fournir un nombre valide.")
