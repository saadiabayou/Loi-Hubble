# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:18:25 2021

@author: Saadia Bayou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:07:55 2021

@author: Saadia Bayou
"""
import matplotlib.pyplot as plt
import numpy as np

# Données :

c=3*1e+8
H0=67.8


# Nombre de galaxie dans l'échantillon 
n_gal=9
# Nombre d'éléments
n_elts=range(1,18)


print("\nCalcul vecteur D distances en Mpc de chaque Galaxie :")

# Distance D

# Données :


# Chargement des données magnétudes
mIa=np.loadtxt("Magnetudes.txt")
#mIa=[15.71,16.39,16.02,15.38,14.54,14.77,13.19,17.37,13.48]
D=[]
def distance(magn):
    return 10**((magn-5.52)/5)

for m in mIa:
    d=round(distance(m),2)
    D.append(d)

print("\nVecteur distance D de l'échantillon de galaxie exprimées Mpc :")
print("\nD=",D, "\n")

print("\nCalcul vecteur vitesse radiale moyenne par Galaxie :")

# Initialisation
vr=[]
vrad=[]

vr_moy=[]
vrad_moy=[]

l0=np.loadtxt("Données_laboratoire_l0.txt")
#l0=[[2200,2350,2580],[2300,2250,2180],[3400,3370,3280],[2100,2250,2280],[2210,2155,2082],[3329,3272,3123],[2127,2450,2386],[2244,2153,2082],[3300,3271,3184]]

print("\nl_laboratoires=",l0)
#print("\ndim l0=",len(l0))
l=np.loadtxt("Données_mesurées_lobs.txt")
#l=[[2250,2370,2610],[2400,2310,2200],[4000,4100,4200],[2300,2551,2596],[2310,2370,2380],[3475,3389,3290],[2210,2565,2682],[2363,2254,2185],[3410,3375,3295]]
#print("\ndim l=",len(l))
print("\nl_observées=",l)
def moyenne(l):
    s=0
    for i in range (len(l)):
        s=s+l[i]
        m=s/(len(l))
        return m

for i in range (len(l)):
    for j in range(len(l[i])):
        v=c*(l[i][j]-l0[i][j])/l0[i][j]
#        print("v=",v)
        vr.append(round(v,2))
    vrad.append(vr)
    vr=[]
print("\nLa matrice des vitesses radiales par Galaxie , v_rad :")
print("\nLa matrice vrad :\n \nvrad= ",vrad)



for i in range(len(l)):
    vr_moy=moyenne(vrad[i])
    vrad_moy.append(round(vr_moy,2))
    
print("\nLe vecteur de vitesse radiale moyenne par Galaxie v_rad_moy:")
print("\nv_rad_moyen=",vrad_moy)   

# Tracé expérimental
plt.scatter(D,vrad_moy, color="r")


# Tracé analytique
H0=67.8
Omega_D=[25,240]
Omega_vrad_moy=[0,2]

d_G=np.linspace(23,250)
#print("\nd_G =",d_G)
u_rad=np.linspace(0,(2*1e+7))
#print("\nu_rad =",u_rad)
u=H0*d_G

plt.plot(d_G,u_rad,color="b")


plt.title("           Vitesse radiale vrad_moy en fonction de la distance D ")
plt.xlabel("D en Mpc")
plt.ylabel("v_rad en Km/s")

plt.savefig("vitesse radiale galaxie en fonction de sa distance D")

plt.show()

# Calcul écart type

vrad_th=[]
for i in range(len(D)):
    v_th=H0*D[i]
#    print("\nv_th =",v_th)
    vrad_th.append(round(v_th,2))

print("\nvrad_théorique",vrad_th)

ec_type=[]    
for i in range(9):
    et=((vrad_th[i]-vrad_moy[i])**2)/9
    ec_type.append(round(et,2))

print("\necart_type= ", ec_type)




## Tracé écart type
#
#plt.plot(ec_type,color="g")














