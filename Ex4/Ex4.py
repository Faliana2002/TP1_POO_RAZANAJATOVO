#!/usr/bin/env python
from math import sin, cos, sqrt
from math import *

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


class Couleur(object):
    def __init__(self, r, v, b):
        self.r = r
        self.v = v
        self.b = b

class Objet3D(object):
    def __init__(self, g:Vecteur, couleur:Couleur):
        self.g = g
        self.couleur = couleur
        self.triangles = [] # Liste de triangles

    def afficher(self):
        print("Le centre de gravité de l'objet est :")
        self.g.afficher()
        print("La couleur de l'objet est : [",self.couleur.r,self.couleur.v,self.couleur.b,"]")
        print("Il est composé de :")
        for triangle in self.triangles:
            triangle.afficher()
    
    def ajouterTriangle(self,triangle):
        self.triangles.append(triangle) # Ajout d'un triangle à la liste
    
    def deplacer(self, vecteur):
        self.g = self.g.additionner(vecteur)
        for triangle in self.triangles:
            triangle.vecteur1 = triangle.vecteur1.additionner(vecteur)
            triangle.vecteur2 = triangle.vecteur2.additionner(vecteur)
            triangle.vecteur3 = triangle.vecteur3.additionner(vecteur)



# Programme principal
def main():

    # Ex4
    g = Vecteur(1,2,3)
    c = Couleur(1,0,0)

    vecteur1 = Vecteur(1,1,1)
    vecteur2 = Vecteur(2,2,2)
    vecteur3 = Vecteur(3,3,3)
    triangle1 = Triangle(vecteur1, vecteur2, vecteur3)
    triangle1.afficher()

    vecteurx = Vecteur(3,2,1)
    vecteury = Vecteur(6,5,4)
    vecteurz = Vecteur(9,8,7)
    triangle2 = Triangle(vecteurx, vecteury, vecteurz)
    print("\n")
    triangle2.afficher()

    objet = Objet3D(g,c)
    objet.ajouterTriangle(triangle1)
    objet.ajouterTriangle(triangle2)
    print("\nAvant déplacement, notre objet est constitué de :")
    objet.afficher()

    x = int(input("\nEntrez un entier x:"))
    y = int(input("Entrez un entier y:"))
    z = int(input("Entrez un entier z:"))
    vecteur = Vecteur(x, y, z)
    objet.deplacer(vecteur)
    print("\nAprès déplacement, notre objet est constitué de :")
    objet.afficher()

if __name__ == "__main__":
    main()

    



