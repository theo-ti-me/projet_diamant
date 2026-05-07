def partage_tresor(montant, joueurs):
    """
    Partage un trésor équitablement entre les joueurs encore actifs.
    Renvoie le reste (gemmes indivisibles) qui reste sur le chemin.
    """
    joueurs_actifs = [j for j in joueurs if j["actif"] == True]
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
    if not isinstance(carte_piochee, str):
        return False
    return carte_piochee in cartes_manche_en_cours

def tresor_retour(montant, joueurs):
    """
    Partage le trésor au sol entre les joueurs qui ont décidé de rentrer
    au camp ce tour (actif == False).
    Renvoie le reste qui reste sur le chemin.
    """
    joueurs_sortants = [j for j in joueurs if not j["actif"] == False]
    if not joueurs_sortants:
        return montant
 
    partage = montant // len(joueurs_sortants)
    reste   = montant % len(joueurs_sortants)
 
    for j in joueurs_sortants:
        j["sac"] += partage
 
    return reste

def rentree_au_camp(joueurs):
    """
    Pour chaque joueur qui rentre (actif == False) :
      - transfère le contenu du sac dans le coffre
      - vide le sac
      - remet actif à True pour la prochaine manche
    """
    for j in joueurs:
        if j["actif"] == False:
            j["coffre"] += j["sac"]
            j["sac"]    = 0
            j["actif"] = "sorti"