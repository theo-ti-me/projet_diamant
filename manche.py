import random
from donnees import generer_deck
from mecaniques import partage_tresor, est_mortel, tresor_retour, rentree_au_camp, ajout_reliques, recuperer_relique

def jouer_manche(joueurs, exclusions, numero_manche, pile_reliques):
    """
    Jouer une manche complete.
    Renvoie les exclusions mises à jour (dangers retires pour les prochaines manches).
    """
    print(f"\n=== MANCHE {numero_manche} ===")

    # 1. préparer le deck
    cartes = generer_deck(exclusions)
    ajout_reliques(cartes, pile_reliques)
    random.shuffle(cartes)

    # 2. remettre tous les joueurs actifs pour cette manche
    for j in joueurs:
        j["is_active"] = True
        j["sac"] = 0

    cartes_manche = [] # carte de la manche déjà sorties
    tresor_sol = 0 # tresor qui s'accumule sur le chemin
    reliques_sol = [] # liste des relique au sol

    # 3. boucle principale
    for c in cartes:
        joueurs_sortants = [] # liste des joueurs qui sorte a ce tour de la manche

        # décision des joueur actifs
        print(f"\nActuellement le totale des trésors au sol est de {tresor_sol}")
        for j in joueurs:
            if j["is_active"] == True:
                choix = input(f"{j['nom']} (sac = {j['sac']}) : continuer ou rentrer ? ").strip().lower()
                if choix == "rentrer":
                    joueurs_sortants.append(j)
                    j["is_active"] = False
    
        # partage du trésor au sol pour ce qui rentre a ce tour
        tresor_sol = tresor_retour(tresor_sol, joueurs_sortants)
        rentree_au_camp(joueurs, numero_manche)

        # Donne les relique au joueur si il est tous seul a sortire 
        if recuperer_relique(joueurs_sortants):
            while reliques_sol:
                relique = int(reliques_sol.pop(0).split("_")[1])
                joueurs_sortants[0]["coffre"][numero_manche - 1] += relique

        # vérifier s'il reste des joueurs actifs
        if not any(j["is_active"] == True for j in joueurs):
            print("Tous les joueurs sont rentrés au camp !")
            break

        # piocher la carte
        print(f"\nCarte piochée : {c}")

        # si c'est une carte danger piocher 2 fois alors fin de la manche
        if est_mortel(c, cartes_manche):
            print(f"Danger '{c}' sorti 2 fois ! Tous le monde perd son sac !")
            for j in joueurs:
                if j["is_active"] == True:
                    j["sac"] = 0
                    j["is_active"] = False
            exclusions[c] += 1  # danger retiré pour les prochaines manches
            break

        # enregistre la carte 
        cartes_manche.append(c)

        # partage des tresor pour les personne encore actif si une carte tresor est piocher
        if c.isdigit():
            tresor_sol += partage_tresor(int(c), joueurs)
            print(f"Trésor ! Chacun reçoit sa part. Le reste au sol : {tresor_sol}")

        # ajout les relique piocher à la liste des reliques
        if c.startswith("R_"):
            reliques_sol.append(c)
        
    return exclusions