def creer_joueur(nom):
    """
    permet de créer un dico pour chaque joueur
    """
    return {"nom": nom, "coffre": [0,0,0,0,0], "sac": 0, "is_active": True, "est_humain": True}

def creer_joueur_ia(nom, ia):
    """
    créer un dico pour les ia
    """
    return {"nom": nom, "coffre": [0,0,0,0,0], "sac": 0, "is_active": True, "est_humain": False, "ia": ia}

def generer_deck(exclusions):
    """
    Cette fonction permet de générer un nouveau deck à chaque manche en retirant
    les cartes qui ont fait perdre lors des manches précédentes.
    "Exclusions" est un dictionnaire qui contient le nombre de fois que la carte doit être enlevée
    """
    deck = ["1","2","3","4","5","5","7","7","9","11","11","13","14","15","17"]
    dangers = ["araignées","serpents","lave","boulets","pics"]
    for d in dangers:
        nb_exemplaires = 3 - exclusions[d]
        for i in range(nb_exemplaires):
            deck.append(d)
    return deck

def creer_pile_reliques():
    return["R_5","R_7","R_8","R_10","R_12"]