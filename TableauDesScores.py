import pygame


class TableauDesScores:
    """ Classe pour l'affichage des scores/compteurs du jeu agar.io. """
    def __init__(self):
        pygame.font.init()
        self.police = (pygame.font.SysFont('Segoe UI', 22))
        self.compteurEnnemis = 0
        self.compteurCreeps = 0

    def dessiner(self, screen, couleurFond):
        """ Méthode qui permet de dessiner le tableau. """
        pygame.draw.rect(screen, couleurFond, pygame.Rect(5, 5, 200, 100))
