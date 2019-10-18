import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import linear_model

import matplotlib.pyplot as plt


def main():
    
    hubble = pd.read_csv("hubble.csv", sep=';')
    print(hubble.head())

    distance = hubble['distance'].values
    velocity = hubble['recession_velocity'].values

    # reshape vector for sklearn method
    distance = distance.reshape(len(distance), 1)
    velocity = velocity.reshape(len(velocity), 1)

if __name__ == '__main__':
    main()
    
    print("That's All, Folks!")
    
    