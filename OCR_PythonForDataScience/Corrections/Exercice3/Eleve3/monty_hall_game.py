import numpy as np
from enum import Enum

class Strategie(Enum):
    CHANGER = 1
    GARDER = 0
    RANDOM = 2

    
def play(strategie, nb_tours):
    
    # simple tableaux des differentes portes
    portes = np.arange(3)
    
    # Tableaux des bonnes portes pour chaque tour
    bonne_portes = np.random.choice(portes, nb_tours)
    
    # Tableaux des premiers choix du joueurs pour chaque tour
    premier_choix = np.random.choice(portes, nb_tours)
    
    # Tableaux des portes restantes pour chaque tours
    p = np.array(list(np.delete(portes, p) for p in premier_choix))
    # p1 = np.fromfunction(lambda i, j: np.delete(portes, premier_choix[i]), (nb_tours, 2), dtype=int)
    
    # Le présentateur élimine une porte
    test = premier_choix == bonne_portes

    def remove_door(l):
        return [np.random.choice(p[i]) if test[i] else bonne_portes[i] for i in l]
        
    p = np.fromfunction(lambda i: remove_door(i), (nb_tours,), dtype=int)

    # Le deuxieme choix depend de la strategie
    if strategie == Strategie.CHANGER:
        deuxieme_choix = p
    elif strategie == Strategie.GARDER:
        deuxieme_choix = premier_choix
    elif strategie == Strategie.RANDOM:
        deuxieme_choix = np.fromiter((np.random.choice([p[i], premier_choix[i]]) for i in range(nb_tours)), dtype=int)
    else:
        raise ValueError(f"Stratégie non reconnue!: {strategie}")

    
    return np.fromiter((1 if t else 0 for t in deuxieme_choix == bonne_portes), dtype=int)