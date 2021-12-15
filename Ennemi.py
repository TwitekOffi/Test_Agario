import random
import pygame
from pygame import Vector2

import core


class Ennemi:
    """ Classe pour les ennemis du jeu agar.io. """

    def __init__(self):

        self.rayon = 5
        self.couleur = (random.randint(40, 240), 0, 0)
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.nom = "ENNEMI"
        self.uuid = random.randint(1000000000, 9999999999999)

        self.direction = Vector2(0, 0)
        self.raideur = 0.00025
        self.vitesse = 1
        self.vitessemax = 2
        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.detecte_Joueur = 0

        self.ChampVisionEnnemi = float(50)
        self.ChampVisionEnnemi_resultat = 0

        self.liste_Percu_E = []
        self.liste_Percu_C = []

        self.Nouvelle_liste2 = []

    def mourir(self):
        """ Méthode qui permet de repositionner les ennemis. → Faire comme s'ils mourraient. """
        self.rayon = 5
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))

    def draw(self, screen):
        """ Méthode qui permet de dessiner les ennemis. """
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
        core.Draw.circle(self.couleur, self.position, self.ChampVisionEnnemi, 1)

    def perception(self, liste_Creep, liste_Ennemi, Joueur):
        """ [PAS FONCTIONNEL] Méthode qui permet aux ennemis d'avoir un champ de vision circulaire. """
        self.liste_Creep = liste_Creep
        self.liste_Ennemi = liste_Ennemi
        self.liste_Percu_E = []
        self.liste_Percu_C = []

        for ennemi in self.liste_Ennemi:
            if self.ChampVisionEnnemi > self.position.distance_to(ennemi.position) and self != ennemi:
                self.liste_Percu_E.append(ennemi)
        for creep in self.liste_Creep:
            if self.ChampVisionEnnemi > self.position.distance_to(creep.position):
                self.liste_Percu_C.append(creep)
        if self.ChampVisionEnnemi > self.position.distance_to(Joueur.position):
            self.detecte_Joueur = 1
        else:
            self.detecte_Joueur = 0

    def grossir(self):
        """ Méthode qui permet aux ennemis de grossir. """
        if self.rayon < 150:
            self.rayon = self.rayon + 1
            self.ChampVisionEnnemi = self.ChampVisionEnnemi + 6

            self.vitessemax = self.vitessemax * 0.988
            self.Fx = self.vitesse * self.Fx

    def deplacement_aleatoire(self, h, l):
        """ Méthode qui permet aux ennemis de se déplacer aléatoirement. """
        self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

        self.direction = self.direction + self.Fx

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

    def fuite(self, h, l):
        """ PAS FONCTIONNEL """
        self.liste_Percu_E.sort(key=lambda x: x.position.distance_to(self.position), reverse=True)

        self.Nouvelle_liste = sorted(self.liste_Percu_E, key=lambda x: x.position.distance_to(self.position),
                                     reverse=True)

        for ennemi in self.Nouvelle_liste:
            self.Ux = ennemi.position - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(0, self.direction.y * -1)

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

    def deplacement_versCreep(self, h, l):
        """ [PAS FONCTIONNEL] Méthode qui permet aux ennemis de trouver et de se déplacer vers les creeps présents
        dans leur champ de vision. """
        self.liste_Percu_C.sort(key=lambda x: x.position.distance_to(self.position), reverse=True)

        self.Nouvelle_liste2 = sorted(self.liste_Percu_C, key=lambda x: x.position.distance_to(self.position),
                                      reverse=True)

        if len(self.Nouvelle_liste2) > 0:
            creep = self.Nouvelle_liste2[0]
            self.Ux = creep.position - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

            if self.direction.length() > self.vitessemax and self.direction.length() != 0:
                self.direction.normalize()
                self.direction.scale_to_length(self.vitessemax)

            self.position = self.direction + self.position

            if self.position.y < 0 or self.position.y > h:
                self.direction = Vector2(0, self.direction.y * -1)

            if self.position.x < 0 or self.position.x > l:
                self.direction = Vector2(self.direction.x * -1, self.direction.y)
