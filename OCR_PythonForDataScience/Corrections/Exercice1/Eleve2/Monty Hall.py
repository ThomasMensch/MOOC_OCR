Python 3.6.4 (v3.6.4:d48ecebad5, Dec 18 2017, 21:07:28) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
%matplotlib inline  \n
import numpy as np\n
import matplotlib.pyplot as plt\n
from math import sqrt, pi, exp\n
choix1 = np.random.randint(3, size=(10000,100)) \n
bonne_porte = np.random.randint(3, size=(10000,100))\n
#Garder
garder = np.sum((choix1 == bonne_porte),0) /10000\n
x=plt.hist(garder, bins=10)\n
#changer
changer = np.sum((choix1 != bonne_porte),0) / 10000\n",
y=plt.hist(changer, bins=10)
