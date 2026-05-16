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
        return len(defausse) > 4