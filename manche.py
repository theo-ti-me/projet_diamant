import random
from donnees import generer_deck
from mecaniques import partage_tresor, est_mortel, tresor_retour, rentree_au_camp, ajout_reliques

def jouer_manche(joueurs, exclusions, numero_manche):
    """
    Jouer une manche complete.
    Renvoie les exclusions mises à jour (dangers retires pour les prochaines manches).
    """
    print(f"\n=== MANCHE {numero_manche} ===")

    # 1. préparer le deck
    cartes = generer_deck(exclusions)
    ajout_reliques(cartes)
    random.shuffle(cartes)

    # 2. remettre tous les joueurs actifs pour cette manche
    for j in joueurs:
        j["actif"] = True
        j["sac"] = 0

    cartes_manche = [] # carte de la manche déjà sorties
    tresor_sol = 0 # tresor qui s'accumule sur le chemin
    relique_sol = [] # liste des relique au sol

    # 3. boucle principale
    for c in cartes:
        joueurs_sortants = [] # liste des joueurs qui sorte a ce tour de la manche

        # décision des joueur actifs
        print(f"\nActuellement le totale des trésors au sol est de {tresor_sol}")
        for j in joueurs:
            if j["actif"] == True:
                choix = input(f"{j['nom']} (sac = {j['sac']}) : continuer ou rentrer ? ").strip().lower()
                if choix == "rentrer":
                    joueurs_sortants.append(j)
                    j["actif"] = False
    
        # partage du trésor au sol pour ce qui rentre a ce tour
        tresor_sol = tresor_retour(tresor_sol, joueurs_sortants)
        rentree_au_camp(joueurs)

        # vérifier s'il reste des joueurs actifs
        if not any(j["actif"] == True for j in joueurs):
            print("Tous les joueurs sont rentrés au camp !")
            break

        # piocher la carte
        print(f"\nCarte piochée : {c}")

        # si c'est une carte danger piocher 2 fois alors fin de la manche
        if est_mortel(c, cartes_manche):
            print(f"Danger '{c}' sorti 2 fois ! Tous le monde perd son sac !")
            for j in joueurs:
                if j["actif"] == True:
                    j["sac"] = 0
                    j["actif"] = "sorti"
            exclusions[c] += 1  # danger retiré pour les prochaines manches
            break

        # enregistre la carte 
        cartes_manche.append(c)

        # partage des tresor pour les personne encore actif si une carte tresor est piocher
        if isinstance(c, int):
            tresor_sol += partage_tresor(c, joueurs)
            print(f"Trésor ! Chacun reçoit sa part. Le reste au sol : {tresor_sol}")
        
    return exclusions