cartes = ["1", "2", "3", "4", "5", "5", "7", "7", "9", "11", "11", "13", "14", "15", "17", "serpents", "boulets", "pics", "araignées", "lave", "serpents", "boulets", "pics", "araignées", "lave", "serpents", "boulets", "pics", "araignées", "lave"]

reliques = ["R_5","R_7","R_8","R_10","R_12"]

pieges = ["serpents", "boulets", "pics", "araignées", "lave"]

class ktourStrategy:
    def __init__(self):
        pass
    def play(self,
             mon_coffre, # liste d'entiers de taille nb_manches
             mon_sac, # entier : nombre de rubis
             rubis_au_sol, # rubis restants à partager
             id_manche, # entier : compris entre 1 et 5
             les_joueurs,    # [ {"coffre":[2,5,0,0,0], "is_active" : True}
                             #,... ,
                             # {"coffre": [0,15,3,0,0], "is_active" : False} ]
             tas_tri, # le tas de cartes restantes (pas dans l'ordre de tirage)
             defausse # ce qui est déjà joué comme cartes
            ):
        
        # calcule la proba des dangers
        risque = 0
        for p in pieges:
            if p in defausse:
                nb_dans_tas = tas_tri.count(p)
                risque += nb_dans_tas / len(tas_tri)

        seuil = 0.3

        # calcule de la position par rapore a la moyenne de tous les joueur
        moyenne_coffre = sum(sum(j["coffre"]) for j in les_joueurs) / len(les_joueurs)
        mon_total = sum(mon_coffre) + mon_sac
        
        if mon_total < moyenne_coffre:
            seuil += 0.1
        elif mon_total > moyenne_coffre:
            seuil -= 0.1
        
        if mon_sac > moyenne_coffre:
            seuil -= 0.1

        nb_actifs = sum(1 for j in les_joueurs if j["is_active"])
        gain_reel = rubis_au_sol // nb_actifs

        # calcul en fonction des rubis au sol
        if gain_reel > moyenne_coffre:
            seuil -= 0.1

        relique_disponible = any(c.startswith("R_") for c in defausse)
        seul_actif = nb_actifs == 1

        #calcule en fonction des reliques
        if relique_disponible:
            valeur_relique = sum(int(c.split("_")[1]) for c in defausse if c.startswith("R_"))

            # si on est seul et que les reliques vale plus que la motié du sac on rentre 
            if seul_actif and valeur_relique > mon_sac * 0.5:
                return False
            
            # mm si on est pas seul mais que les relique vale le coup on baisse le seuil
            if valeur_relique > moyenne_coffre:
                seuil -= 0.1

        # calcul gain espere
        somme_tresors_tas = sum(int(c) for c in tas_tri if c.isdigit())

        gain_espere = somme_tresors_tas / nb_actifs
        if gain_espere > mon_sac:
            seuil += 0.1
        elif gain_espere < mon_sac:
            seuil -= 0.1


        seuil = max(0.1, seuil) # bloque le seuil à 0.1

        return risque < seuil