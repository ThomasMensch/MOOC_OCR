# Module contenant la fonction simulant un certain nombre de parties du jeu Monty Hall

# Importation des modules nécessaires
import numpy as np
from enum import Enum

# Ici nous définissons une sous-classe de Enum, qui contiendra les stratégies possibles.
class Strategie(Enum):
    CHANGER = int(1)
    GARDER = 2
    ALEATOIRE = 3

    
def play(strategie, nb_tours):
    '''Simule une suite de tours du jeu Monty Hall.
    
    Cette fonction renvoie les résultats de plusieurs parties
    du jeu Monty Hall sous forme d'une liste de gains par le 
    joueur.
    
    Args:
        strategie (Strategie): La strategie du joueur
        nb_tours (int): Nombre de tours
        
    Returns:
        array: Tableau des gains du joueurs à chaque partie
    '''
    
    # Initialisation des bonnes portes    
    bonne_porte = np.random.randint(0,3,nb_tours)
    
    # Initialisation des choix du joueur    
    premier_choix = np.random.randint(0,3,nb_tours)
    
    # Tableau qui contient True aux endroits où le premier choix est la bonne porte, False ailleurs    
    etat_intermediaire = np.equal(bonne_porte, premier_choix)

    # Le présentateur enlève une porte QUI N'EST PAS LA BONNE et donc maintenant, tout dépend de la stratégie    
    res = 0 # Variable qui contiendra le résultat
    
    if strategie == Strategie.CHANGER: # Changer : on gagne partout où on avait PAS fait le bon choix, on perd sinon
        
        # On met 1 pour les cas gagnants, 0 pour les cas perdants
        res = np.where(etat_intermediaire == False, 1, 0) 
    
    elif strategie == Strategie.GARDER: # Garder : on gagne partout où on avait fait le bon choix, on perd sinon
        
        # On met 1 pour les cas gagnants, 0 pour les cas perdants
        res = np.where(etat_intermediaire == True, 1, 0) 
    
    elif strategie == Strategie.ALEATOIRE: # Aleatoire : on choisit l'une ou l'autre aléatoirement
        
        # Les évènements précédents ne changent rien, on choisit de manière aléatoire (loi uniforme) une porte ou l'autre
        # On met toujours 1 pour les cas gagnants, 0 pour les cas perdants
        res = np.random.randint(0,2,nb_tours)
    
    else:
        raise ValueError('Stratégie non reconnue!')
    
    return(res)
