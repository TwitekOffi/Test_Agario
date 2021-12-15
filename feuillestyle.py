# ==================================================================================================================== #
# --→ Code écrit par Arnaud MORMONT.                                                                                   #
# --→ Objectif de ce fichier: Paramétrer la feuille de style de chaque objet de l'interface graphique(PyQt5) → Menu    #
#     et du chargement qui précède l'affichage du menu principal.                                                      #
# --→ Ce fichier appartient au projet du cours d'informatique qui a lieu dans le cadre de la licence professionnelle   #
#     RAVI | Promo 2021-2022. Ce projet est dirigé en binôme par Arnaud MORMONT et Matéo ROLLET.                       #
# --→ L'interface graphique et le chargement ont été codés par Arnaud MORMONT sous PyQt5.                              #
# ==================================================================================================================== #

class FeuilleDeStyle:
    """ Définit le style de tous les objets du menu. """

    feuille_style = """
    
    /* Style des objets du chargement */
          
        #chargement_fond
        { background-color: rgb(56, 58, 89);
          color: rgb(220, 220, 220);
          border-radius: 10px }
          
        #chargement_titre
        { color: rgb(0, 255, 217) }
        
        #barre_chargement { background-color: rgb(98, 114, 164); color: rgb(200, 200, 200); border-style: none; 
        border-radius: 10px; text-align: center } 
        #barre_chargement::chunk { border-radius: 10px; background-color: 
        qlineargradient(spread:pad, x1:0, y1:0.54, x2:1, y2:0.545273, stop:0 rgba(0, 255, 217, 255), stop:1 rgba(0, 
        153, 255, 255)) }
        
        #texte_chargement
        { color: rgb(98, 114, 164) }
    
    /* Style des objets du menu principal */
    
    
        #fond
        { background-color: rgb(56, 58, 89);
          color: rgb(220, 220, 220);
          border-radius : 20px }
        
        #ligne_h
        { background-color: rgb(0, 255, 217) }
        
        #ligne_b
        { background-color: rgb(0, 255, 217) }
        
        #titre { color: rgb(0, 255, 217) }
        
        #soustitre { color: rgb(98, 114, 164) }
        
        #credits { color: rgb(98, 114, 164) }
        
        #indic_pseudo { color: rgb(98, 114, 164) }
        
        #entree_pseudo 
        { border-radius:10px;
          border:1px solid rgb(0, 238, 202);
          background-color: rgb(81, 84, 129);
          color: rgb(0, 255, 174) }
        #entree_pseudo:hover
        { border:3px solid rgb(0, 238, 202); }
        #entree_pseudo:focus
        {border:3px solid rgb(0, 238, 202) }
        
        #indic_mode_diff { color: rgb(98, 114, 164) }
        
        #chck_mode_diff::indicator 
        { width: 32px;
          height: 32px }
        #chck_mode_diff::indicator:checked 
        { image: url(W:/infoRavi/AgarIO/chk_ok.png) }
        #chck_mode_diff::indicator:unchecked 
        { image: url(W:/infoRavi/AgarIO/chk_nok.png) }
        
        #indic_mode_sombre { color: rgb(98, 114, 164) }
        
        
        #chck_mode_sombre::indicator 
        { width: 32px;
          height: 32px }
        #chck_mode_sombre::indicator:checked 
        { image: url(W:/infoRavi/AgarIO/chk_ok.png) }

        #chck_mode_sombre::indicator:unchecked 
        { image: url(W:/infoRavi/AgarIO/chk_nok.png) }
        
        #bouton_jouer 
        { background-color: rgb(98, 114, 164);
          border: none;
          color: rgb(0, 255, 217);
          border-left: 1px solid rgb(126, 148, 212);
          border-right: 1px solid rgb(126, 148, 212);
          border-bottom: 3px solid rgb(126, 148, 212) }
        #bouton_jouer:hover
        { background-color: rgb(117, 137, 197);
          color: rgb(187, 255, 221);
          border-left: 1px solid rgb(148, 175, 249);
          border-right: 1px solid rgb(148, 175, 249);
          border-bottom: 3px solid rgb(148, 175, 249) }
        #bouton_jouer:pressed
        { background-color: rgb(152, 179, 255);
          color: rgb(187, 255, 221);
          border-left: 1px solid rgb(117, 137, 197);
          border-right: 1px solid rgb(117, 137, 197);
          border-bottom: 3px solid rgb(117, 137, 197) }
    
    """