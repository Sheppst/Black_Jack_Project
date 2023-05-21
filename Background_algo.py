from random import randint

cartes = []
nom = ["C", "Ca", "T", "P"]
for i in range(4):
    for j in range(1, 14):
        cartes.append((j, nom[i]))


class Jeu:

    def __init__(self, Joueur):
        self.Joueur = Joueur
        self.croupier = []
        self.somme = 0
        self.cartes = cartes[:]

    def lancer_partie(self):
        for i in range(2):
            variable = randint(0, len(self.cartes) - 1)
            if self.cartes[variable][0] == 11:
                ajouter = ("V", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 12:
                ajouter = ("Q", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 13:
                ajouter = ("K", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            else:
                self.croupier.append(self.cartes[variable])
                self.somme += self.cartes[variable][0]
                del self.cartes[variable]
            if i == 0:
                somme_avant = self.somme

        rep = int(input("Quel est votre mise ?"))
        while rep > self.Joueur.argent:
            rep = int(
                input(
                    "Vous n'avez pas assez d'argent, veuillez entrez une autre mise"
                ))
        self.Joueur.argent += -rep
        self.Joueur.mise = rep
        print("Première carte du croupier:" + str(self.croupier[0]) + " somme : " + str(somme_avant))
        self.Joueur.distribuer()
        return self.comparaison()

    def reinitialisation_carte(self):
        self.cartes = cartes[:]

    def reinitialisation_joueur(self):
        self.Joueur.cartes_joueur = []

    def reinitialisation_croupier(self):
        self.croupier = []

    def reinitialisation_mise_somme(self):
        self.somme = 0
        self.Joueur.mise = 0
        self.Joueur.somme_cartes = 0

    def reinitialisation(self):
        self.reinitialisation_carte()
        self.reinitialisation_joueur()
        self.reinitialisation_croupier()
        self.reinitialisation_mise_somme()

        rep = int(
            input("Voulez vous continuez de jouer ? il vous reste : " +
                  str(self.Joueur.argent)))
        print(rep)
        if rep == 1:
            return self.lancer_partie()
        elif rep == 2:
            print("voici votre argent : " + str(self.Joueur.argent))

    def comparaison(self):
        while self.somme < 17:
            variable = randint(0, len(self.cartes) - 1)
            if self.cartes[variable][0] == 11:
                ajouter = ("V", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 12:
                ajouter = ("Q", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 13:
                ajouter = ("K", self.cartes[variable][1])
                self.croupier.append(ajouter)
                self.somme += 10
                del self.cartes[variable]
            else:
                self.croupier.append(self.cartes[variable])
                self.somme += self.cartes[variable][0]
                del self.cartes[variable]
        if self.Joueur.somme_cartes > 21:
            print("Vous avez perdu vos cartes sont " + str(self.Joueur.cartes_joueur) + " somme : " + str(
                self.Joueur.somme_cartes))
            return self.reinitialisation()

        if self.Joueur.somme_cartes == 21:
            if self.somme == 21:
                print("BlackJack, mais pour le croupier aussi,Egalité, vous recupérez votre mise")
            else:
                self.Joueur.argent += self.Joueur.mise * 2
                print("BlackJack, vous avez gagné , les cartes du croupier sont : " + str(
                    self.croupier) + ", somme : " + str(self.somme))
                return self.reinitialisation()

        if self.somme > 21 or self.somme < self.Joueur.somme_cartes:
            self.Joueur.argent += self.Joueur.mise * 2
            print("Vous avez gagné , les cartes du croupier sont : " + str(self.croupier) + ", somme : " + str(
                self.somme))
            return self.reinitialisation()
        if self.somme == self.Joueur.somme_cartes:
            self.Joueur.argent += self.Joueur.mise
            print("Egalité, vous recupérez votre mise, les cartes du croupier sont : " + str(
                self.croupier) + ", somme : " + str(self.somme))
            return self.reinitialisation()
        print("Vous avez perdu, les cartes du croupier sont : " + str(self.croupier) + ", somme : " + str(self.somme))
        return self.reinitialisation()


class Joueur:

    def __init__(self, argent):
        self.argent = argent
        self.cartes_joueur = []
        self.mise = 0
        self.somme_cartes = 0
        self.cartes = cartes[:]

    def distribuer(self):
        """ Ajoute a cartes joueurs deux cartes au hasard, et leur somme. """
        for i in range(2):
            variable = randint(0, len(self.cartes) - 1)
            if self.cartes[variable][0] == 11:
                ajouter = ("V", self.cartes[variable][1])
                self.cartes_joueur.append(ajouter)
                self.somme_cartes += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 12:
                ajouter = ("Q", self.cartes[variable][1])
                self.cartes_joueur.append(ajouter)
                self.somme_cartes += 10
                del self.cartes[variable]
            elif self.cartes[variable][0] == 13:
                ajouter = ("K", self.cartes[variable][1])
                self.cartes_joueur.append(ajouter)
                self.somme_cartes += 10
                del self.cartes[variable]
            else:
                self.cartes_joueur.append(self.cartes[variable])
                self.somme_cartes += self.cartes[variable][0]
                del self.cartes[variable]
        if self.depasse() != True:
            print("vos cartes sont " + str(self.cartes_joueur) + " somme : " +
                  str(self.somme_cartes))
            rep2 = int(input("voulez vous doubler la mise?"))
            if rep2 == 1:
                return self.doubler_mise()
            rep = int(input("Voulez vous tirer? "))
            if rep == 1:
                self.tirer()
        else:
            print("Vous avez depassé ")

    def tirer(self):
        variable = randint(0, len(self.cartes) - 1)
        if self.cartes[variable][0] == 11:
            ajouter = ("V", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        elif self.cartes[variable][0] == 12:
            ajouter = ("Q", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        elif self.cartes[variable][0] == 13:
            ajouter = ("K", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        else:
            self.cartes_joueur.append(self.cartes[variable])
            self.somme_cartes += self.cartes[variable][0]
            del self.cartes[variable]
        if self.somme_cartes == 21:
            return None
        if self.depasse() != True:
            print("vos cartes sont " + str(self.cartes_joueur) + " somme : " +
                  str(self.somme_cartes))
            rep = int(input("Voulez vous tirer? "))
            if rep == 1:
                self.tirer()
        else:
            print("Vous avez depassé ")

    def depasse(self):
        if self.somme_cartes > 21:
            return True

    def doubler_mise(self):
        variable = randint(0, len(self.cartes) - 1)
        if self.cartes[variable][0] == 11:
            ajouter = ("V", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        elif self.cartes[variable][0] == 12:
            ajouter = ("Q", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        elif self.cartes[variable][0] == 13:
            ajouter = ("K", self.cartes[variable][1])
            self.cartes_joueur.append(ajouter)
            self.somme_cartes += 10
            del self.cartes[variable]
        else:
            self.cartes_joueur.append(self.cartes[variable])
            self.somme_cartes += self.cartes[variable][0]
            del self.cartes[variable]
        if self.depasse() != True:
            print("vos cartes sont " + str(self.cartes_joueur) + " somme : " +
                  str(self.somme_cartes))


moi = Joueur(500)
partie = Jeu(moi)
partie.lancer_partie()
