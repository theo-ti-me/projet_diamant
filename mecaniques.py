def partage_tresor(montant, joueurs):
    """
    Partage un trésor équitablement entre les joueurs encore actifs.
    Renvoie le reste (gemmes indivisibles) qui reste sur le chemin.
    """
    joueurs_actifs = [j for j in joueurs if j["is_active"] == True]
    if not joueurs_actifs:
        return montant

    partage = montant // len(joueurs_actifs)
    reste = montant % len(joueurs_actifs)

    for j in joueurs_actifs:
       j["sac"] += partage

    return reste

def est_mortel(carte_piochee, cartes_manche_en_cours):
    """
    Renvoie True si la carte est un danger ET qu'elle est déjà apparue
    dans la manche (doublée → tout le monde perd).
    """
    if carte_piochee.startswith("R_"): # verifi que ce n'est pas une relique
        return False
    if carte_piochee.isdigit(): # verifi que ce n'est pas un tresore
        return False
    return carte_piochee in cartes_manche_en_cours

def tresor_retour(montant, joueurs_sortants):
    """
    Partage le trésor au sol entre les joueurs qui ont décidé de rentrer
    au camp ce tour.
    Renvoie le reste qui reste sur le chemin.
    """
    if not joueurs_sortants:
        return montant
 
    partage = montant // len(joueurs_sortants)
    reste   = montant % len(joueurs_sortants)
 
    for j in joueurs_sortants:
        j["sac"] += partage
 
    return reste

def rentree_au_camp(joueurs, id_manche):
    """
    Pour chaque joueur qui rentre (is_active == False) :
      - transfère le contenu du sac dans le coffre
      - vide le sac
      - remet is_active à True pour la prochaine manche
    """
    for j in joueurs:
        if j["is_active"] == False:
            j["coffre"][id_manche - 1] += j["sac"]
            j["sac"] = 0

def ajout_reliques(deck, pile_reliques):
    relique = pile_reliques.pop(0)
    deck.append(relique)

def recuperer_relique(joueurs_sortants):
    """
    retourne vrais si une personne est seul à sortire et peux récupérer la ou les reliques
    """
    return len(joueurs_sortants) == 1