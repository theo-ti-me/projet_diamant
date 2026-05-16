from donnees import creer_joueur, creer_pile_reliques, creer_joueur_ia
from manche import jouer_manche
from ia import ktourStrategy

def init_joueurs():
    """
    Initialise la liste des joueurs
    """
    joueurs = []

    nb_humains = int(input("Entrez le nombre de joueur humains (minimum 1 et maximum 8) : ").strip())
    for i in range(nb_humains):
        nom = input(f"\nNom du joueur {i+1} : ")
        j = creer_joueur(nom)
        joueurs.append(j)

    nb_ia = int(input("Entrez le nombre de joueur IA à ajouter :"))
    nb_total = nb_humains + nb_ia
    while nb_total < 3 or nb_total > 8:
        print("\nNombre de joueur incorecte il faut être minimum 3 et maximum 8.")
        nb_ia = int(input("Redonner un nombre d'ia correcte : "))
        nb_total = nb_humains + nb_ia
    for i in range(nb_ia):
        nom = f"IA_{i + 1}"
        ia = ktourStrategy()
        j = creer_joueur_ia(nom, ia)
        joueurs.append(j)
    return joueurs

def jouer_partie(joueurs):
    # dictionnaire des danger exclue
    exclusions = {"araignées": 0,"serpents": 0,"lave": 0,"boulets": 0,"pics": 0}

    pile_reliques = creer_pile_reliques()

    id_manche = 1

    while id_manche < 6:
        exclusions = jouer_manche(joueurs, exclusions, id_manche, pile_reliques)


        print(f"\nFin de la manche {id_manche}, voici l'état de vos coffres.")
        for j in joueurs:
            print(f"\n{j['nom']} : {sum(j['coffre'])}")
        id_manche += 1


    classement = sorted(joueurs, key=lambda j: sum(j["coffre"]), reverse=True)

    print("\nFin de la dernière manche. Voici le classement")
    ordre = 1
    for j in classement:
        print(f"\n{ordre} : {j['nom']} ({j['coffre']})")
        ordre += 1

