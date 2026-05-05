def partage_tresor(montant, joueurs):
    """
    Partage les trésore si les joueur son encore actife
    renvoi se qui doit rester au sol
    """
    joueur_actif = 0
    for j in joueurs:
        if j["actif"] == 1:
            joueur_actif += 1
    partage = montant // joueur_actif
    reste = montant % joueur_actif
    for j in joueurs:
        if j["actif"] == 1:
            j["sac"] += partage
    return reste

def est_mortel(carte_piochee, cartes_sorties):
    """
    Renvoi vrai si une carte fais perdre la manche
    """
    if carte_piochee in cartes_sorties:
        return True
    return False

def tresor_retour(montant, joueurs):
    """
    Partage les trésore si les joueur deside de retourner au camp
    renvoi se qui doit rester au sol
    """
    joueur_sortant = 0
    for j in joueurs:
        if j["actif"] == 0:
            joueur_sortant += 1
    partage = montant // joueur_sortant
    reste = montant % joueur_sortant
    for j in joueurs:
        if j["actif"] == 0:
            j["sac"] += partage
    return reste

def rentree_au_camp(joueur):
    """
    mets les tresor du sac dans le coffre
    """
    for j in joueur:
        tresor = j["sac"]
        j["coeffre"] += tresor
        j["sac"] = 0
        j["actif"] = 1

