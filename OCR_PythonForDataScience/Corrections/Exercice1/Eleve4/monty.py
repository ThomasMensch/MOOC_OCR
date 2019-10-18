import numpy as np

def generate_monty_hall(change=True, samples=1000):
    good_doors = np.random.randint(1, 4, samples)
    random_choices = np.random.randint(1, 4, samples)
    first_choice_res = good_doors == random_choices
    if change:
        return ~first_choice_res
    return first_choice_res
    