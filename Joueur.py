import random
import pygame
from pygame import Vector2
import core


class Joueur:
    """ Classe pour le joueur du jeu agar.io. """

    def __init__(self):
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.couleur = self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rayon = 5
        self.rayon_max = 150

        self.raideur = 0.00035
        self.vitesse = 1
        self.vitessemax = 5
        self.direction = Vector2(0, 0)
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0
        self.Fx = 0

        # Variables couleurs print
        self.reset = "\033[0m"
        self.gras = "\033[1m"

        self.rouge = "\033[31m"
        self.rouge_clair = "\033[91m"

    def grossir(self):
        """ Méthode qui permet au joueur de grossir. """
        if self.rayon < 150:
            self.rayon = self.rayon + 1

            self.vitessemax = self.vitessemax * 0.988
            self.Fx = self.vitesse * self.Fx

    def mourir(self):
        """ Actions faites lorsque le joueur est mangé, lorsqu'il meurt. """
        # self.rayon = 2
        print(self.gras + self.rouge_clair + f' → Fin de la partie de {core.memory("PseudoChoisi")}.' + self.reset)
        print(self.gras + self.rouge + 'Partie terminée: Vous avez perdu!\n' + self.reset)
        exit()

    def draw(self, screen):
        """ Méthode qui dessine le joueur. """
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
        # screen.blit(screen, self.nom, self.position)

    def deplacer(self, clic, h, l):
        """ Méthode qui permet au joueur de se déplacer. """
        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)
            self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if clic is not None:

            self.Ux = clic - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)

            self.Fx = self.raideur * self.L * self.Ux
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)

        if self.direction.length() > self.vitessemax and self.direction.length() != 0:
            self.direction.normalize()
            self.direction.scale_to_length(self.vitessemax)

        self.position = self.direction + self.position
