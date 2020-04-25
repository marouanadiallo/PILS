#encoding:utf-8
import tkinter as tk
from tkinter import messagebox
from vue.Accueil import Accueil
from vue.CreationJoueur import CreationJoueur
from vue.Entrainement import Entrainement
from datas.donnees_vue import NOM_DU_JEU, PATH_ICO


class Vue(tk.Tk):
    """
    """
    
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self._controller = controller
        
        
        self.definiton_proprietes_fenetre_principale()      #Appelle définition des proprietés de la fenetre principale
        self.vue_accueil()                                  #Appelle de la vue d'accueil
        
    
    
    def vue_accueil(self):
        """
            Crée la vue d'accueil et ajoute des boutons du menu principal
        """
        self._vue_accueil = Accueil(self)
        self._vue_accueil.creation_bouton_entrainement("Entrainement", lambda:self._controller.activer_vue_creer_joueur(1))        #ajout du bouton entrainement
        self._vue_accueil.creation_bouton_jeu_a_deux("Jeu à deux", lambda:self._controller.activer_vue_creer_joueur(2))                                                              #ajout du bouton jeu à deux
        self._vue_accueil.creation_bouton_quitter("Quitter", self.quit)                                                          #ajout du bouton quitté l'application
    
        self._vue_accueil.pack(expand="yes") 
        
    def cacher_vue_accueil(self):
        self._vue_accueil.pack_forget()
        
    def vue_creer_joueur(self, fn_callback):
        """
            Cette méthode affiche la vue créer un joueur (en gros s'enrengistrer)
        """
        self._vue_creer_joueur = CreationJoueur(self)
        self._vue_creer_joueur.bouton_creer("commencer une partie", lambda:fn_callback(self._vue_creer_joueur._pseudo.get()))
        
        self._vue_creer_joueur.pack(expand="yes")
    
    def cacher_vue_creer_joueur(self):
        self._vue_creer_joueur.pack_forget() 
    
    def vue_entrainement(self):
        """
        """
        self._vue_entrainement = Entrainement(self, self._controller)
        self._vue_entrainement.pack()
        
    def supp_vue_entrainement(self):
        """
            cette méthode supprime totalement la vue d'entrainement actif
        """
        self._vue_entrainement.destroy()
        
    def definiton_proprietes_fenetre_principale(self):
        """
            Cette methode définit les propriétés de la fénêtre principale
        """
        #On recupère la taille de l'ecran de l'appareil correspondant
        screen_x =  self.winfo_screenwidth()
        screen_y =  self.winfo_screenheight()

        TAILLE_WIN = (screen_x//2,screen_y//2+((screen_y//2)//4))        #la fenêtre aura pour taille la moitié de l'écran de l'appareil d'exécution

        #afin de centrer la fenêtre au lancement 
        pos_x = (screen_x // 2)-(TAILLE_WIN[0] //2)
        pos_y = (screen_y // 2)-(TAILLE_WIN[1] // 2)

        POS_WIN = (pos_x, pos_y)                    #définition de la position initiale
        
        self.title(NOM_DU_JEU)
        #self.iconbitmap(PATH_ICO)
        geo = "{}x{}+{}+{}".format(TAILLE_WIN[0], TAILLE_WIN[1], POS_WIN[0], POS_WIN[1])
        self.geometry(geo)
        self.resizable(width = False, height = False)
        
        
    def lance_alerte(self, msg):
        """
            Lance un messagebox info
        """
        messagebox.showinfo("Inforamtion", msg)