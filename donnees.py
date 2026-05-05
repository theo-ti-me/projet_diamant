def creer_joueur(nom):
    """
    permet de créer un dico pour chaque joueur
    actif : 1 -> il est dans la grote, O -> il est en train de rentree, -1 -> il est a la base
    """
    return {"nom": nom, "coffre": 0, "sac": 0, "actif": 1}

def generer_deck(exclutions):
    """
    Cette fonction permet de générer un nouveau deck à chaque manche en retirant
    les cartes qui ont fait perdre lors des manches précédentes.
    "Exclusions" est un dictionnaire qui contient le nombre de fois que la carte doit être enlevée
    """
    deck = [1,2,3,4,5,5,7,7,9,11,11,13,14,15,17]
    dangers = ["scorpions","serpents","lave","pierre","piques"]
    for d in dangers:
        nb_exemplaires = 3 - exclutions[d]
        for i in range(nb_exemplaires):
            deck.append(d)
    return deck