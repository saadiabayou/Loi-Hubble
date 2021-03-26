# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:09:42 2021

@author: Saadia Bayou
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import matplotlib.pyplot as plt
import numpy as np

# Distance D

# Données :
mIa=[15.71,16.39,16.02,15.38,14.54,14.77,13.19,17.37,13.48]
D=[]
def distance(magn):
    return 10**((magn-5.52)/5)

for m in mIa:
    d=round(distance(m),2)
    D.append(d)

print("\nVecteur distance D de l'échantillon de galaxie exprimées Mpc :")
print("\nD=",D)

n_gal=2
n_raie=3
#Vitesse radiale
# Initailisation
c=3*10e+6
v_rad=[]
Mv=np.zeros((n_raie,n_gal))
print("\nMv=",Mv)
print("\n")
s=0
# Tests - valeurs alé tests
l0=[1100,2900,4000]
# Matrice raies Galaxie
#rG=[[6548,6563,6584],[6548,6584]]
l=[]
r=[l0,[1000, 3000,5000], [2000,4000]]



for i in range (len(r)):
    print(r[i])
    for j in range(len(r[i])):
        vr=c*(r[i][j]-r[0][j])       
        v_rad.append(vr)
        print("\nvrad =",v_rad)
     
def moyenne(l):
    s=0
    for i in range (len(l)):
        s=s+l[i]
        m=s/(len(l))
        print("moyenne=",m)

# Appel fonction 
