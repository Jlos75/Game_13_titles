

def afficher_titres(titres):
    print("\n Titres restants :")
    for numero, titre in titres.items():
        print(f"  {numero}. {titre}")
    print()


def choisir_titre(titres):
    while True:
        try:
            choix = input("Choisis un titre (numéro) : ").strip()
            numero = int(choix)
            if numero in titres:
                return numero
            print("Ce numéro n'existe pas ou n'est plus disponible.")
        except ValueError:
            print("Entre un nombre valide.")


def lancer_jeu():
    titres = {
        1: "Titre 1",
        2: "Titre 2",
        3: "Titre 3",
        4: "Titre 4",
        5: "Titre 5",
        6: "Titre 6",
        7: "Titre 7",
        8: "Titre 8",
        9: "Titre 9",
        10: "Titre 10",
        11: "Titre 11",
        12: "Titre 12",
        13: "Titre 13",
    }

    print("=== Jeu des 13 titres ===")
    print("Règle : chaque équipe choisit un titre.")
    print("Le rang 12 donne le plus de points, le rang 1 donne le moins.")
    print("Si une équipe prend le dernier titre 13, l'autre equipe prend les points restants.")

    noms = input("Entre les noms des équipes séparés par une virgule : ").strip()
    equipes = [nom.strip() for nom in noms.split(',') if nom.strip()]

    if not equipes:
        print("Tu dois entrer au moins une équipe.")
        return

    score = {equipe: 0 for equipe in equipes}
    tour = 1

    while len(titres) > 0:
        print(f"\n=== Tour {tour} ===")
        afficher_titres(titres)

        for equipe in equipes:
            if len(titres) == 0:
                break

            print(f"\nC'est au tour de l'équipe {equipe}.")
            numero = choisir_titre(titres)
            titre_choisi = titres.pop(numero)

            if len(titres) == 0:
                print(f"{equipe} a pris le dernier titre : elle perd !")
                print("Fin du jeu.")
                print("\nScores finaux :")
                for nom, pts in score.items():
                    print(f"- {nom} : {pts} points")
                return

            points = 14 - numero
            score[equipe] += points
            print(f"{equipe} a choisi {titre_choisi} (rang {numero}) et gagne {points} points.")

        tour += 1

    print("\nTous les titres ont été joués sans perdre de dernier titre.")
    print("Scores finaux :")
    for nom, pts in score.items():
        print(f"- {nom} : {pts} points")


if __name__ == "__main__":
    lancer_jeu()
