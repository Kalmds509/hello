from random import randrange
import pickle
import os
# Essayer de charger le dictionnaire depuis le fichier s'il existe
if os.path.exists("scores.txt"):
    with open("scores.txt", "r") as file:
        scores_data = file.read()
    scores_dict = {}
    if scores_data:
        for line in scores_data.split('\n'):
            if line:
                parts = line.split(',')
                if len(parts) == 2:  # Vérifiez qu'il y a deux parties (pseudo et score)
                    pseudo, score = parts[0], int(parts[1])
                    scores_dict[pseudo] = score
else:
    scores_dict = {}
epsedo = input("Antre epsedo ou pou ka komanse jwet la : ")
while not epsedo.islower() or " " in epsedo:
    epsedo = input("ERROR li pa korek: ")
# Vérifier si le joueur existe dans le dictionnaire
if epsedo in scores_dict:
    sko = scores_dict[epsedo]  # Récupérer le score précédent
else:
    sko = 0
while True:
    nonb_aleyatwa = randrange(1, 10)
    print(nonb_aleyatwa)
    chans = 3
    while chans > 0:
        chwa_itilizate = input(f"Hello {epsedo}, kounya chwazi yon nonb ant 1 a 10: ")

        while int(chwa_itilizate) < 1 or int(chwa_itilizate) > 10:
            chwa_itilizate = input("Ou chwazi yon nonb ki pa nan enteval la. Rechwazi: ")

        if int(chwa_itilizate) == nonb_aleyatwa:
            print("BRAVO")
            nouvo_sko = chans * 30  # Calcul du nouveau score
            print(f"Ancien skò: {sko}")
            print(f"Nouvo skò: {sko+nouvo_sko}")
            sko += nouvo_sko  # Mettre à jour le score actuel
            break
        else:
            chans -= 1
            if int(chwa_itilizate) > nonb_aleyatwa:
                print(f"vre nonb lan pi piti ke sa ou sot chwazi an.Ou ret {chans} chans")
            elif int(chwa_itilizate) < nonb_aleyatwa:
                print(f"vre nonb lan pi gro ke sa ou sot chwazi an.Ou ret {chans} chans")
            if chans == 0:
                print("Ou pa ret chans anko. Ou pedi.")
                print(f"Nonb kache a se te: {nonb_aleyatwa}")
    avi = input("Press 'k' to stop the game, or any other key to continue: ")
    if avi.lower() == "k":
        break
# Mettre à jour le dictionnaire avec le pseudonyme et le score
scores_dict[epsedo] = sko
# Enregistrez le dictionnaire mis à jour dans le fichier au format CSV
with open("scores.txt", "w") as file:
    for pseudo, score in scores_dict.items():
        file.write(f"{pseudo},{score}\n")

