hauteur = 0
largeur = 0
estOk = 0
difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()

while estOk == 0 :
    if difficulte == "FACILE":
            hauteur += 6
            largeur += 6

            estOk = 1
            continue
    elif difficulte == "MOYEN":
            hauteur += 8
            largeur += 8
            estOk = 1
            continue
    elif difficulte == "DIFFICILE":
            hauteur += 11
            largeur += 11
            estOk = 1
            continue
    else:
            print("Mauvais")
            difficulte = input("Capitaine, quel niveau choisissez-vous ? Facile, moyen, difficile ?").upper()
            estOk = 0