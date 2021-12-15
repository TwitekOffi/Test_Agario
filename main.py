# ==================================================================================================================== #
# --→ Code écrit par Arnaud MORMONT.                                                                                   #
# --→ Objectif de ce fichier: Fichier global. C'est ici que l'on compile tous les fichiers du projet.                  #
# --→ Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle   #
#     RAVI | Promo 2021-2022. Ce projet est dirigé en binôme par Arnaud MORMONT et Matéo ROLLET.                       #
# --→ L'interface graphique et le chargement ont été codés par Arnaud MORMONT sous PyQt5.                              #
# ==================================================================================================================== #

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from MenuPyQt import MenuPyQt

from chargement_agario import ChargementAgario

# Déclaration compteur pour chargement
compteur = 0


# FENÊTRE CHARGEMENT
########################################################################################################################

class Chargement(QMainWindow):
    """ Classe du chargement avant le lancement du menu principal d'agar.io. """
    def __init__(self):
        QMainWindow.__init__(self)
        self.chargement_anime = ChargementAgario()
        self.chargement_anime.setup(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Retirer le cadre et le titre de la fenêtre.
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Rendre le fond de la fenêtre transparent/invisible.

        # DÉBUT Qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # Qtimer en ms
        self.timer.start(35)

        # Afficher la fenêtre
        self.show()

    def progress(self):
        """Méthode qui permet d'animer la barre de chargement et d'afficher le menu principal à la fin du chargement."""
        global compteur
        # VALEUR DE LA BARRE DE CHARGEMENT
        self.chargement_anime.barre_chargement.setValue(compteur)

        # FERMER LE CHARGEMENT ET OUVRIR LE MENU PRINCIPAL
        if compteur > 100:
            # Arrêter le timer
            self.timer.stop()

            # Ouvrir menu principal
            self.menu = MenuPyQt()
            self.menu.show()

            # Fermer la fenêtre de chargement
            self.close()

        # Augmenter la valeur du compteur → animation chargement
        compteur = compteur + 1


# Boucle d'affichage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = Chargement()
    sys.exit(app.exec_())
