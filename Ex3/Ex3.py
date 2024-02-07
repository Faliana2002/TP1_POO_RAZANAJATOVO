#!/usr/bin/env python3
from math import sin, cos, sqrt, pi

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

class Triangle(object):
    def __init__(self, vecteur1:Vecteur, vecteur2:Vecteur, vecteur3:Vecteur):
        self.vecteur1 = vecteur1
        self.vecteur2 = vecteur2
        self.vecteur3 = vecteur3
    
    def tourner(self, alpha):
        alpha_rad = alpha * pi / 180
        self.turnvecteur1x = self.vecteur1.x*cos(alpha_rad) - self.vecteur1.y*sin(alpha_rad)
        self.turnvecteur1y = self.vecteur1.y*sin(alpha_rad) + self.vecteur1.y*cos(alpha_rad)
        self.vecteur1.x = self.turnvecteur1x
        self.vecteur1.y = self.turnvecteur1y

        self.turnvecteur2x = self.vecteur2.x*cos(alpha_rad) - self.vecteur2.y*sin(alpha_rad)
        self.turnvecteur2y = self.vecteur2.y*sin(alpha_rad) + self.vecteur2.y*cos(alpha_rad)
        self.vecteur2.x = self.turnvecteur2x
        self.vecteur2.y = self.turnvecteur2y

        self.turnvecteur3x = self.vecteur3.x*cos(alpha_rad) - self.vecteur3.y*sin(alpha_rad)
        self.turnvecteur3y = self.vecteur3.y*sin(alpha_rad) + self.vecteur3.y*cos(alpha_rad)
        self.vecteur3.x = self.turnvecteur3x
        self.vecteur3.y = self.turnvecteur3y


    def deplacer(self,vecteur):
        self.vecteur1.x = self.vecteur1.x + vecteur.x
        self.vecteur1.y = self.vecteur1.y + vecteur.y
        self.vecteur1.z = self.vecteur1.z + vecteur.z

        self.vecteur2.x = self.vecteur2.x + vecteur.x
        self.vecteur2.y = self.vecteur2.y + vecteur.y
        self.vecteur2.z = self.vecteur2.z + vecteur.z

        self.vecteur3.x = self.vecteur3.x + vecteur.x
        self.vecteur3.y = self.vecteur3.y + vecteur.y
        self.vecteur3.z = self.vecteur3.z + vecteur.z

    def afficher(self):
        print("Le triangle est composé des vecteurs : \n[",self.vecteur1.x, self.vecteur1.y, self.vecteur1.z,"] \n[",self.vecteur2.x, self.vecteur2.y, self.vecteur2.z,"] \n[",self.vecteur3.x, self.vecteur3.y, self.vecteur3.z,"]")


# Programme principal
def main():
    # Ex3
    vecteur1 = Vecteur(1,2,3)
    vecteur2 = Vecteur(4,5,6)
    vecteur3 = Vecteur(7,8,9)
    triangle = Triangle(vecteur1, vecteur2, vecteur3)
    print("Avant rotation, on a:")
    triangle.afficher()
    alpha = 45
    triangle.tourner(alpha)
    print("\nAprès rotation de ",alpha,"degré, on a:")
    triangle.afficher()

    x = int(input("\nEntrez un entier x:"))
    y = int(input("Entrez un entier y:"))
    z = int(input("Entrez un entier z:"))
    vecteur = Vecteur(x, y, z)
    triangle.deplacer(vecteur)
    print("\nAprès déplacement de [",vecteur.x, vecteur.y, vecteur.z,"], on a :")
    triangle.afficher()

if __name__ == "__main__":
    main()
