from donnees import creer_joueur
from manche import jouer_manche

def init_joueurs():
    """
    Initialise la liste des joueurs
    """
    nb_joueur = int(input("Entrez le nombre de joueur (minimum 3 et maximum 8) : ").strip())
    while nb_joueur < 3 or nb_joueur > 8:
        print("\nNombre de joueur incorecte il faut être minimum 3 et maximum 8.")
        nb_joueur = int(input("Redonner un nombre de joueur corecte : "))
    joueurs = []
    for i in range(nb_joueur):
        nom = input(f"\nEntrez le nom du joueur {i+1} : ")
        j = creer_joueur(nom)
        joueurs.append(j)
    return joueurs

def jouer_partie(joueurs):
    #dictionnaire des danger exclue
    exclusions = {"scorpions": 0, "serpents": 0, "lave": 0, "pierre":0, "piques": 0}

    id_manche = 1

    while id_manche < 6:
        exclusions = jouer_manche(joueurs, exclusions, id_manche)


        print(f"\nFin de la manche {id_manche}, voici l'état de vos coffres.")
        for j in joueurs:
            print(f"\n{j['nom']} : {j['coffre']}")
        id_manche += 1
    
    classement = sorted(joueurs, key=lambda j: j["coffre"], reverse=True)

    print("\nFin de la dernière manche. Voici le classement")
    ordre = 1
    for j in classement:
        print(f"\n{ordre} : {j['nom']} ({j['coffre']})")
        ordre += 1

