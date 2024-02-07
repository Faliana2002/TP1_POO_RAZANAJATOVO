#!/usr/bin/env python3
from math import sin, cos, sqrt
from math import *

# Exercice 2
class Vecteur(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def additionner(self, vecteur):
        # Important pour pouvoir réutiliser directement les valeurs additinnées
        return Vecteur(self.x + vecteur.x, self.y + vecteur.y, self.z + vecteur.z)
    
    def calculerNorme(self):
        self.norme = sqrt(self.x**2 + self.y**2 + self.z**2)
        print("La norme du vecteur [",self.x,self.y,self.z,"] est ",self.norme)

    def calculerProduitScalaire(self, vecteur):
        self.ps = self.x*vecteur.x + self.y*vecteur.y + self.z*vecteur.z

    def tourner(self, alpha):
        alpha_rad = alpha * pi / 180
        self.turnx = self.x*cos(alpha_rad) - self.y*sin(alpha_rad)
        self.turny = self.y*sin(alpha_rad) + self.y*cos(alpha_rad)
        self.x = self.turnx
        self.y = self.turny
    
    def afficher(self):
        print("[",self.x, self.y, self.z,"]")


# Programme principal
def main():

    # Exo2
    xinit = 0
    yinit = 0
    zinit = 0
    vecteur = Vecteur(xinit, yinit, zinit)
    print("Le vecteur nul est : ")
    vecteur.afficher()

    x1 = int(input("Entrez un entier x1 :"))
    y1 = int(input("Entrez un entier y1 :"))
    z1 = int(input("Entrez un entier z1 :"))
    vecteur1 = Vecteur(x1, y1, z1)
    x2 = int(input("Entrez un entier x2 :"))
    y2 = int(input("Entrez un entier y2 :"))
    z2 = int(input("Entrez un entier z2 :"))
    vecteur2 = Vecteur(x2, y2, z2)
    vecteurr = vecteur1.additionner(vecteur2)
    print("La somme des deux vecteurs est : ")
    vecteurr.afficher()

    vecteur1.calculerNorme()

    alpha = int(input("Entrez un angle en degré :"))
    vecteur1.tourner(alpha)
    print("Après rotation, on obtient le vecteur :")
    vecteur1.afficher()

if __name__ == "__main__":
    main()