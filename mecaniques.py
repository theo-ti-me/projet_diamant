def partage_tresor(montant, joueurs):
    joueur_actif = 0
    for j in joueurs:
        if j["actif"] == True:
            joueur_actif += 1
    partage = montant // joueur_actif
    reste = montant % joueur_actif
    for j in joueurs:
        if j["actif"] == True:
            j["sac"] += partage
    return reste
