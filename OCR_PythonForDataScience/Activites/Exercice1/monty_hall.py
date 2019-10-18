'''
Activite 1 du MOOC Decouvrez les librairies python pour la Data Science (OpenClassRoom)
'''

import numpy as np
import matplotlib.pyplot as plt
from enum import Enum

class Strategie(Enum):
    GARDER = 0
    CHANGER = 1

def play(strategie, nb_tours=100000, seed=None):
    '''Simule une suite de tours du jeu de Monty Hall.
    
    Cette fonction retourne un tableau des gains du joueur pour un nombre de tours donne

    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours [defaut=100000]
        seed (int): Pour eventuellement controler la generation des nombre aleatoires
    Returns:
        gains: gains du joueurs sous forme de tableau numpy
    '''
    portes = [1, 2, 3]

    if seed is not None:
        np.random.seed(seed)
    
    # tirer aleatoirement la bonne porte pour chaque tour
    bonne_porte = np.random.choice(portes, size=nb_tours)
    
    # tirer aleatoirement le choix du joueur
    premier_choix = np.random.choice(portes, size=nb_tours)

    # construire le tableau des gains en fonction de la strategie choisie(GARDER vs. CHANGER)
    if strategie == Strategie.GARDER:
        # Dans ce cas, le joueur gagne s'il A FAIT le bon choix au depart
        gains = (premier_choix == bonne_porte)
    else: # strategie = Strategie.CHANGER
        # Dans ce cas, le joueur gagne s'il N'A PAS FAIT le bon choix au depart
        gains = (premier_choix != bonne_porte)
        
    return gains

if __name__ == '__main__':
    
    nb_tours = 100000

    gains_changer = play(Strategie.GARDER, nb_tours)
    gains_garder = play(Strategie.CHANGER, nb_tours)

    print("En changeant de porte, le joueur a gagne {} sur {} parties."
          .format(np.sum(gains_changer), nb_tours))
      
    print("En gardant son choix initial, le joueur a gagne {} sur {} parties."
          .format(np.sum(gains_garder), nb_tours))
