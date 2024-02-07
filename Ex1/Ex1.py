#!/usr/bin/env python3

# Exercice 1
class Algebre(object):
    # Définition du constructeur
    def __init__(self, n):
        self.n = n

    # Méthode pour la somme des n premiers entiers
    def add(self):
        self.sum = 0
        for self.i in range (1, self.n + 1):
            self.sum = self.sum + self.i
        
        print("La somme des ",self.n,"premiers éléments est ",self.sum)
    
    # Méthode pour le factoriel des n premiers entiers sans le 0
    def factoriel(self):
        self.fact = 1
        for self.j in range (1, self.n + 1):
            self.fact = self.fact * self.j
        
        print("Le factoriel des ",self.n,"premiers éléments est ",self.fact)

# Programme principal
def main():
    # Ex1
    n = int(input("Entrez un entier positif :"))
    algebre = Algebre(n)
    algebre.add()
    algebre.factoriel()

if __name__ == "__main__":
    main()