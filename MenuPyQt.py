# ==================================================================================================================== #
# --→ Code écrit par Arnaud MORMONT.                                                                                   #
# --→ Objectif de ce fichier: Créer un menu prnicipal pour le jeu agar.io(pygame) avec une interface graphique(PyQt5)  #
# --→ Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle   #
#     RAVI | Promo 2021-2022. Ce projet est dirigé en binôme par Arnaud MORMONT et Matéo ROLLET.                       #
# --→ L'interface graphique → Le menu a été entièrement codée par Arnaud MORMONT.                                      #
# ==================================================================================================================== #

import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QSize
from PyQt5.QtGui import QCursor, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QLineEdit, QCheckBox, QPushButton, QApplication

from feuillestyle import FeuilleDeStyle

from agario import demarrer_jeu


class MenuPyQt(QMainWindow):
    """ Menu princpal du jeu. """

    def __init__(self):
        super(QMainWindow, self).__init__()

        # Taille de la fenêtre principale
        self.resize(680, 400)

        # Suppression du "window tittle" et fond de la fenêtre transparent
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Police utilisée pour toutes les indications de choix
        self.police_indic = QFont()
        self.police_indic.setFamily("Segoe UI")
        self.police_indic.setPointSize(14)

        # Construction du menu
        self._init_fond()
        self._init_ligne_h()
        self._init_ligne_b()

        self._init_titre()
        self._init_soustitre()
        self._init_credits()

        self._init_indic_choix_pseudo()
        self._init_entree_pseudo()

        self._init_indic_mode_diff()
        self._init_checkbox_mode_diff()

        self._init_indic_mode_sombre()
        self._init_checkbox_mode_sombre()

        self._init_bouton_jouer()

        # Variables utilisées pour les choix du joueur via le menu
        self.nbennemis = 5
        self.couleur_fond_jeu = (255, 255, 255)
        self.couleur_fond_scores = (230, 230, 230)
        self.couleur_police_scores = (0, 0, 0)
        self.couleur_grille = (150, 150, 150)

        # Bouton Jouer
        self.bouton_jouer.clicked.connect(self.clic_jouer)

        # Bouton difficulté
        self.chck_diff.clicked.connect(self.clic_activer_difficile)

        # Bouton mode sombre (darkmode)
        self.chck_sombre.clicked.connect(self.clic_activer_darkmode)

        # Afficher le menu
        self.show()

    def _init_fond(self):
        """ Méthode de création du fond de la fenêtre. """
        # Ajout fond de la fenêtre
        self.fond = QFrame(self)
        self.fond.setObjectName('fond')
        self.fond.resize(680, 400)
        self.fond.setCursor(QCursor(Qt.ArrowCursor))
        self.fond.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_ligne_h(self):
        """ Méthode de création de la ligne du haut du menu. """
        # Ligne du haut
        self.ligne_h = QLabel(self.fond)
        self.ligne_h.setObjectName('ligne_h')
        self.ligne_h.setGeometry(QRect(60, 80, 550, 1))
        self.ligne_h.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_ligne_b(self):
        """ Méthode de création de la ligne du bas du menu. """
        # Ligne du bas
        self.ligne_b = QLabel(self.fond)
        self.ligne_b.setObjectName('ligne_b')
        self.ligne_b.setGeometry(QRect(60, 260, 550, 1))
        self.ligne_b.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_titre(self):
        """ Méthode de création du titre du menu. """
        # Titre
        self.titre = QLabel(self.fond)
        self.titre.setObjectName('titre')
        self.titre.setGeometry(QRect(0, 15, 660, 50))

        self.police_titre = QFont()
        self.police_titre.setFamily("Segoe UI")
        self.police_titre.setPointSize(40)

        self.titre.setFont(self.police_titre)
        self.titre.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.titre.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.titre.setText("<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\""
                           ">Agar</span><span style=\" font-size:22pt;\">.io</span></p></body></html>")

    def _init_soustitre(self):
        """ Méthode de création du sous titre du menu. """
        # Sous titre
        self.soustitre = QLabel(self.fond)
        self.soustitre.setObjectName('soustitre')

        self.soustitre.setGeometry(QRect(0, 90, 660, 30))
        self.soustitre.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.police_soustitre = QFont()
        self.police_soustitre.setFamily("Segoe UI")
        self.police_soustitre.setPointSize(13)

        self.soustitre.setFont(self.police_soustitre)
        self.soustitre.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.soustitre.setText("<html><head/><body><p><span style=\" font-size:13pt; font-weight:600;\""
                               ">Licence pro RAVI</span><span style=\" font-size:13pt;\"> - Projet du cours "
                               "d'informatique</span></p></body></html>")

    def _init_credits(self):
        """ Méthode de création des crédits du menu. """
        # Credits
        self.credits = QLabel(self.fond)
        self.credits.setObjectName('credits')

        self.credits.setGeometry(QRect(10, 370, 640, 20))

        self.police_credits = QFont()
        self.police_credits.setFamily("Segoe UI")
        self.police_credits.setPointSize(10)

        self.credits.setFont(self.police_credits)
        self.credits.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.credits.setText(QCoreApplication.translate("MenuPyQt", "<strong>Cr\u00e9\u00e9 par</strong>: "
                                                                    "Arnaud MORMONT \u2022 Mat\u00e9o "
                                                                    "ROLLET", None))

        self.credits.setAlignment(Qt.AlignRight | Qt.AlignTop | Qt.AlignTrailing)

    def _init_indic_choix_pseudo(self):
        """ Méthode qui écrit le texte pour indiquer le choix du pseudo via le menu. """
        # Indication choix pseudo
        self.pseudo = QLabel(self.fond)
        self.pseudo.setObjectName('indic_pseudo')
        self.pseudo.setGeometry(QRect(150, 130, 280, 30))

        self.pseudo.setFont(self.police_indic)
        self.pseudo.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.pseudo.setText(QCoreApplication.translate("MenuPyQt", "<html><head/><body><p align=\"justify\">"
                                                                   "<span style=\" font-size:11pt; "
                                                                   "color:#00ffd9;\">\u2022 </span><span style=\" "
                                                                   "font-size:11pt;\">Choix du </span><span style=\" "
                                                                   "font-size:11pt; font-weight:600;\">pseudo</span>"
                                                                   "<span style=\" font-size:11pt;\">:</span></p>"
                                                                   "</body></html>", None))

    def _init_entree_pseudo(self):
        """ Méthode qui créer l'objet(QLineEdit) dédié au choix du pseudo via le menu. """
        # Entrée pseudo
        self.entree_pseudo = QLineEdit(self.fond)
        self.entree_pseudo.setObjectName('entree_pseudo')
        self.entree_pseudo.setGeometry(QRect(310, 130, 180, 28))
        self.police_entree_pseudo = QFont()
        self.police_entree_pseudo.setPointSize(9)
        self.entree_pseudo.setFont(self.police_entree_pseudo)

        self.entree_pseudo.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.entree_pseudo.setMaxLength(18)
        self.entree_pseudo.setAlignment(Qt.AlignCenter)

        self.entree_pseudo.setText(QCoreApplication.translate("MenuPyQt", "Pseudo par défaut", None))

    def _init_indic_mode_diff(self):
        """ Méthode qui écrit le texte pour indiquer le choix du mode difficile via le menu. """
        # Indication du choix mode difficile
        self.mode_diff = QLabel(self.fond)
        self.mode_diff.setObjectName('indic_mode_diff')
        self.mode_diff.setGeometry(QRect(150, 170, 281, 31))

        self.mode_diff.setFont(self.police_indic)
        self.mode_diff.setStyleSheet("color: rgb(98, 114, 164);")

        self.mode_diff.setText(QCoreApplication.translate("MenuPyQt", "<html><head/><body><p align=\"justify\">"
                                                                      "<span style=\" font-size:11pt; color:#00ffd9;"
                                                                      "\">\u2022 </span><span style=\" "
                                                                      "font-size:11pt;"
                                                                      " color:#6272a4;\">Activer le mode </span>"
                                                                      "<span style=\" font-size:11pt; "
                                                                      "font-weight:600;\">difficile</span><span "
                                                                      "style=\" font-size:11pt;\">:</span></p></body>"
                                                                      "</html>", None))

    def _init_checkbox_mode_diff(self):
        """ Méthode qui créer l'objet(QCheckBox) dédié au choix du mode difficile via le menu. """
        # Bouton mode difficile
        self.chck_diff = QCheckBox(self.fond)
        self.chck_diff.setObjectName('chck_mode_diff')

        self.chck_diff.setGeometry(QRect(380, 170, 32, 32))
        self.chck_diff.setCursor(QCursor(Qt.PointingHandCursor))

        self.chck_diff.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_indic_mode_sombre(self):
        """ Méthode qui écrit le texte pour indiquer le choix du mode sombre via le menu. """
        # Indication du choix mode sombre
        self.mode_sombre = QLabel(self.fond)
        self.mode_sombre.setObjectName('indic_mode_sombre')
        self.mode_sombre.setGeometry(QRect(150, 210, 281, 31))

        self.mode_sombre.setFont(self.police_indic)
        self.mode_sombre.setStyleSheet(FeuilleDeStyle.feuille_style)

        self.mode_sombre.setText(QCoreApplication.translate("MenuPyQt", "<html><body><p align=\"justify\">"
                                                                        "<span style=\" font-size:11pt; color:"
                                                                        "#00ffd9;\">\u2022 </span><span style=\" "
                                                                        "font-size:11pt; color:#6272a4;\">Activer "
                                                                        "le mode </span><span style=\" "
                                                                        "font-size:11pt; font-weight:600; color:"
                                                                        "#6272a4;\">sombre</span><span style=\" "
                                                                        "font-size:11pt; color:#6272a4;\">:</span>"
                                                                        "</p></body></html>", None))

    def _init_checkbox_mode_sombre(self):
        """ Méthode qui créer l'objet(QCheckBox) dédié au choix du mode sombre via le menu. """
        # Bouton mode sombre
        self.chck_sombre = QCheckBox(self.fond)
        self.chck_sombre.setObjectName('chck_mode_sombre')

        self.chck_sombre.setGeometry(QRect(380, 210, 32, 32))
        self.chck_sombre.setCursor(QCursor(Qt.PointingHandCursor))

        self.chck_sombre.setStyleSheet(FeuilleDeStyle.feuille_style)

    def _init_bouton_jouer(self):
        """ Méthode qui créer l'objet(QPushButton) dédié au lancement du jeu(agario.py) via le menu. """
        # Bouton Jouer
        self.bouton_jouer = QPushButton(self.fond)
        self.bouton_jouer.setObjectName('bouton_jouer')
        self.bouton_jouer.setGeometry(QRect(205, 295, 250, 45))

        self.police_bjouer = QFont()
        self.police_bjouer.setFamily("Segoe UI")
        self.police_bjouer.setPointSize(14)
        self.police_bjouer.setBold(True)
        self.police_bjouer.setWeight(75)

        self.bouton_jouer.setFont(self.police_bjouer)
        self.bouton_jouer.setCursor(QCursor(Qt.ArrowCursor))
        self.bouton_jouer.setText(QCoreApplication.translate("MenuPyQt", " Jouer", None))

        self.bouton_jouer.setStyleSheet(FeuilleDeStyle.feuille_style)

        # Icone du bouton Jouer
        icone_b_jouer = QIcon()
        icone_b_jouer.addFile("../../infoRavi/AgarIO/controller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bouton_jouer.setIcon(icone_b_jouer)
        self.bouton_jouer.setIconSize(QSize(32, 32))

    def clic_jouer(self):
        """ Méthode qui s'éxecute lorsque le joueur clic sur le bouton Jouer. """
        self.close()
        demarrer_jeu(self.entree_pseudo.text(), self.nbennemis, self.couleur_fond_jeu, self.couleur_fond_scores,
                     self.couleur_police_scores, self.couleur_grille)

    def clic_activer_difficile(self):
        """ Méthode qui s'éxecute lorsque le joueur clic sur le bouton d'activation du mode difficile. """
        if self.chck_diff.isChecked():
            self.nbennemis = 10
            print(f"\n[CHOIX] Mode difficile activé !\n"
                  f"        Nombre d'ennemis → {self.nbennemis}")
        else:
            self.nbennemis = 5
            print(f"\n[CHOIX] Mode difficile désactivé !\n"
                  f"        Nombre d'ennemis → {self.nbennemis}")

    def clic_activer_darkmode(self):
        """ Méthode qui s'éxecute lorsque le joueur clic sur le bouton d'activation du mode sombre. """
        if self.chck_sombre.isChecked():
            self.couleur_fond_jeu = (40, 40, 40)
            self.couleur_fond_scores = (25, 25, 25)
            self.couleur_police_scores = (255, 255, 255)
            self.couleur_grille = (100, 100, 100)
            print(f"\n[CHOIX] Mode sombre activé ! \n"
                  f"        Couleur du fond → {self.couleur_fond_jeu}\n"
                  f"        Couleur du fond des scores → {self.couleur_fond_scores}\n"
                  f"        Couleur de la police → {self.couleur_police_scores}\n"
                  f"        Couleur de la grille → {self.couleur_grille}")
        else:
            self.couleur_fond_jeu = (255, 255, 255)
            self.couleur_fond_scores = (230, 230, 230)
            self.couleur_police_scores = (0, 0, 0)
            self.couleur_grille = (150, 150, 150)
            print(f"\n[CHOIX] Mode sombre désactivé ! \n"
                  f"        Couleur du fond → {self.couleur_fond_jeu}\n"
                  f"        Couleur du fond des scores → {self.couleur_fond_scores}\n"
                  f"        Couleur de la police → {self.couleur_police_scores}\n"
                  f"        Couleur de la grille → {self.couleur_grille}")


# Design Pattern pour execution du code de la fenêtre principale
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fen = MenuPyQt()
    sys.exit(app.exec_())
