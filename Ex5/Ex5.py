#!/usr/bin/env python3
import random

class De(object):
    def __init__(self):

        # Variable vide
        self.valeur = None

    def lancer(self):
        self.valeur = random.randint(1, 6)
        return self.valeur

class Joueur(object):
    def __init__(self, nom):
        self.nom = nom
        self.des = [De(), De(), De()]
        self.points = 0

    def lancer_des(self):
        return [de.lancer() for de in self.des]

    def relancer_des(self, indices):
        for index in indices:
            self.des[index].lancer()

class Jeu(object):
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def verifier_combinaison(self, valeurs):
        # Ici valeurs sera triée avec .sort()
        valeurs.sort()
        
        # Cas combinaison (4, 2, 1)
        if valeurs == [1, 2, 4]:
            return 10
        
        # Cas où il y a deux "1" parmi les trois dés
        # Ici .count retourne le nombre d'element de la liste avec la valeur 1
        elif valeurs.count(1) == 2:
            return valeurs[2]  # Retourne la valeur du troisième dé
        
        
        # Cas des trois chiffres consécutifs
        elif valeurs[2] - valeurs[1] == 1 and valeurs[1] - valeurs[0] == 1:
            return 2
        return 0

    def jouer_tour(self):
        for joueur in self.joueurs:
            print("\nTour de ",joueur.nom)
            valeurs = joueur.lancer_des()
            print("Résultat du lancer: ",valeurs)
            decision = input("Voulez-vous relancer des dés ? (o/n) ")
            if decision.lower() == 'o':

                # Ici, on sépare les éléments saisis par le joueur, chacun séparé d'un ","
                indices = input("Quels dés voulez-vous relancer ? (0, 1, 2) ").split(',')
                indices = [int(index) for index in indices]
                joueur.relancer_des(indices)
                valeurs = [de.valeur for de in joueur.des]
                print("Nouveau lancer: ",valeurs)
            points = self.verifier_combinaison(valeurs)
            joueur.points += points
            print(joueur.nom," gagne ",points," points, total: ",joueur.points," points")

    def lancer_jeu(self):
        nb_tours = int(input("Combien de tours ? "))
        for _ in range(nb_tours):
            self.jouer_tour()
        self.afficher_gagnant()

    def afficher_gagnant(self):
        if not self.joueurs:  # Vérifie si la liste des joueurs est vide
            print("Aucun joueur n'a été ajouté au jeu.")
            return

        gagnant = max(self.joueurs, key=lambda joueur: joueur.points)
        if gagnant.points > 0:
            print(f"\nLe gagnant est {gagnant.nom} avec {gagnant.points} points!")
        else:
            print("\nAucun joueur n'a gagné de points.")


# Exemple d'utilisation
if __name__ == "__main__":
    jeu = Jeu()
    jeu.ajouter_joueur(Joueur("Alice"))
    jeu.ajouter_joueur(Joueur("Bob"))
    jeu.lancer_jeu()
