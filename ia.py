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
        
        dangers_dangereux = 0
        for p in pieges:
            if p in defausse and p in tas_tri:
                dangers_dangereux += 1

        if id_manche <= 2:
            seuil = 3
        elif id_manche <= 4:
            seuil = 2
        else:
            seuil = 1

        moyenne_coffre = sum(sum(j["coffre"]) for j in les_joueurs) / len(les_joueurs)
        mon_total = sum(mon_coffre) + mon_sac
        
        if mon_total < moyenne_coffre:
            seuil += 1
        elif mon_total > moyenne_coffre:
            seuil -= 1

        seuil = max(1, seuil)

        return dangers_dangereux < seuil