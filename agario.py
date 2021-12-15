# ==================================================================================================================== #
# --→ Code écrit par Arnaud MORMONT et Matéo ROLLET                                                                    #
# --→ Objectif de ce fichier: Avoir un jeu agar.io respectant le cahier des charges établi en cours.                   #
# --→ Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle   #
#     RAVI. Ce projet est dirigé en binôme par Arnaud MORMONT et Matéo ROLLET.                                         #
# --→ Le jeu a été codé par Matéo ROLLET et Arnaud MORMONT.                                                            #
# ==================================================================================================================== #

import pygame
import core

from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur
from TableauDesScores import TableauDesScores


# Variables de couleurs pour prints
reset = "\033[0m"
gras = "\033[1m"
dim = "\033[2m"
souligne = "\033[4m"
clignote = "\033[5m"
inverse = "\033[7m"
cache = "\033[8m"

defaut = "\033[39m"
noir = "\033[30m"
rouge = "\033[31m"
vert = "\033[32m"
jaune = "\033[33m"
bleu = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
gris_clair = "\033[37m"
gris_fonce = "\033[90m"
rouge_clair = "\033[91m"
vert_clair = "\033[92m"
jaune_clair = "\033[93m"
bleu_clair = "\033[94m"
magenta_clair = "\033[95m"
cyan_clair = "\033[96m"
blanc = "\033[97m"


def setup(pseudo, nb_ennemis, couleur_fond_jeu, couleur_fond_scores, couleur_police_scores, couleur_grille):
    """ Définit les variables nécessaires pour le jeu agar.io. """

    print(gras + cyan_clair +
          "\n     ══════════════════════════════════════════════"
          "\n     ╠ → Démarrage d'Agar.io - MORMONT • ROLLET ← ╠\n"
          "     ══════════════════════════════════════════════" + reset)

    print(souligne + magenta_clair + "\nInitialisation des variables...\n" + reset)
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    # INITIALISATIONS VARIABLES INDÉPENDANTES DU JOUEUR

    # Choix des paramètres du joueur via menu principal
    # core.memory("nbennemis", MenuParam().nbennemis)

    # Tableau des scores
    core.memory("TableauDesScores", TableauDesScores())
    core.memory("TextTabScores", "texte vide")

    # Joueur
    core.memory("Joueur", Joueur())

    # Creeps
    core.memory("TableauDeCreeps", [])
    for i in range(150):
        core.memory("TableauDeCreeps").append(Creep())

    # Ennemis
    core.memory("TableauEnnemis", [])
    for i in range(nb_ennemis):
        core.memory("TableauEnnemis").append(Ennemi())

    # Taille de la grille
    core.memory("TailleGrille", 90)

    core.memory("PseudoChoisi", pseudo)
    core.memory("couleurdufond", couleur_fond_jeu)
    core.memory("couleurdufondscore", couleur_fond_scores)
    core.memory("couleurpolicescore", couleur_police_scores)
    core.memory("couleurgrille", couleur_grille)

    # Affichage de tout le dictionnaire
    # afficher_contenu_memory(core.memory("affichage_dico", "Dico affiché"))

    print(souligne + magenta_clair + "\nInitialisation des variables terminé!\n" + reset)

    print(gras + jaune_clair + f'\n → Démarrage de la partie de {core.memory("PseudoChoisi")}.\n' + reset)


def afficher_contenu_memory(dico):
    """ Permet d'afficher toutes les variables contenues dans le dictionnaire de core.memory. """
    return [print(bleu + f'    • clef: {k}, valeur: {v}, type:{type(v)}') for k, v in dico.items()]


def run():
    """ Utilise toutes les variables du setup pour créer et faire fonctionner le jeu agar.io. """
    core.cleanScreen()

    # FOND DE LA FENÊTRE DU JEU
    ####################################################################################################################
    # Dessin du fond
    pygame.draw.rect(core.screen, core.memory("couleurdufond"), pygame.Rect(0, 0, 1080, 720))

    # Dessin de la grille
    for x in range(0, 1080, core.memory("TailleGrille")):
        for y in range(0, 720, core.memory("TailleGrille")):
            rect = pygame.Rect(x, y, core.memory("TailleGrille"), core.memory("TailleGrille"))
            pygame.draw.rect(core.screen, core.memory("couleurgrille"), rect, 1)

    # Bloc collisions
    # ======================================================================================================
    for c in core.memory("TableauDeCreeps"):
        # [Collision] Joueur mange Creeps
        if c.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + c.rayon:
            c.mourir()
            core.memory("Joueur").grossir()
            core.memory("TableauDesScores").compteurCreeps = core.memory("TableauDesScores").compteurCreeps + 1

        # [Collision] Ennemis mangent Creeps
        for ennemi in core.memory("TableauEnnemis"):
            ennemi.perception(core.memory("TableauDeCreeps"), core.memory("TableauEnnemis"), core.memory("Joueur"))
            # if e.ChampVisionEnnemi_resultat == 1:
            # e.deplacement_versCreep(720, 1080, c)
            if c.position.distance_to(ennemi.position) < ennemi.rayon + c.rayon:
                c.mourir()
                ennemi.grossir()



    # [Collision] Ennemis/Joueur
    for ennemi in core.memory("TableauEnnemis"):
        if ennemi.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + ennemi.rayon:
            # Joueur mange ennemis
            if core.memory("Joueur").rayon >= ennemi.rayon:
                ennemi.mourir()
                core.memory("Joueur").grossir()
                core.memory("TableauDesScores").compteurEnnemis = core.memory("TableauDesScores").compteurEnnemis + 1
            # Ennemis mangent joueur
            else:
                core.memory("Joueur").mourir()

    # Bloc dessins
    # =========================================================================================================
    # Dessins des creeps
    for c in core.memory("TableauDeCreeps"):
        c.draw(core.screen)

    # Dessins des ennemis
    for dessin_e in core.memory("TableauEnnemis"):
        dessin_e.draw(core.screen)

    # Dessin du joueur
    core.memory("Joueur").draw(core.screen)

    # Bloc déplacements
    # ====================================================================================================
    # Déplacements du joueur
    core.memory("Joueur").deplacer(core.getMouseLeftClick(), 720, 1080)

    # Déplacements des ennemis (si aucune détection) → déplacements aléatoires
    for deplacementsEnnemis in core.memory("TableauEnnemis"):

        # deplacementsEnnemis.deplacement_aleatoire(720, 1080)
        deplacementsEnnemis.deplacement_versCreep(720, 1080)
        # e.deplacement_versCreep(720,1080,c)

    # Bloc scores
    # ====================================================================================================
    # Dessin du rectangle pour les scores
    core.memory("TableauDesScores").dessiner(core.screen, core.memory("couleurdufondscore"))

    # Affichage du pseudo choisi par le joueur
    core.memory("TextTabScores",
                core.memory("TableauDesScores").police.render("Joueur: " + str(core.memory("PseudoChoisi")), False,
                                                              core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 4))

    # Affichage du rayon du joueur
    core.memory("TextTabScores",
                core.memory("TableauDesScores").police.render("Rayon du joueur: " + str(core.memory("Joueur").rayon),
                                                              False, core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 26))

    # Affichage des creeps mangés par le joueur
    core.memory("TextTabScores", core.memory("TableauDesScores").police.render(
        "Creeps mangés: " + str(core.memory("TableauDesScores").compteurCreeps), False,
        core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 48))

    # Affichage des ennemis mangés par le joueur
    core.memory("TextTabScores", core.memory("TableauDesScores").police.render(
        "Ennemis mangés: " + str(core.memory("TableauDesScores").compteurEnnemis), False,
        core.memory("couleurpolicescore")))
    core.screen.blit(core.memory("TextTabScores"), (8, 70))

    if core.memory("Joueur").rayon == Joueur().rayon_max:
        print(gras + vert_clair + f' → Fin de la partie de {core.memory("PseudoChoisi")}.' + reset)
        print(vert + f'Partie terminée: Vous avez atteint le rayon maximum! | Rayon max = {Joueur().rayon_max}\n' +
              reset)
        exit()


def demarrer_jeu(pseudo, nb_ennemis, couleur_fond_jeu, couleur_fond_scores, couleur_police_scores, couleur_grille):
    """ Permet de démarrer le jeu avec les paramètres définis dans le menu principal. """
    core.main(setup(pseudo, nb_ennemis, couleur_fond_jeu, couleur_fond_scores, couleur_police_scores, couleur_grille),
              run)
