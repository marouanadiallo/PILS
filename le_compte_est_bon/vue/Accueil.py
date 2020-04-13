#encoding:utf-8
from tkinter import Frame, Label, StringVar
from vue.Bouton import Bouton
from datas.donnees_vue import NOM_DU_JEU, DESCRIPTION

class Accueil(Frame):
    """
        cette classe définie les widgets de la vue d'accueil de l'application
    """
    
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.label_nom_du_jeu()
        self.label_description()
    
    
    
    def creation_bouton_entrainement(self, label="Entrainement", fn_callback=None):
        self._entrainement = Bouton(self, label, fn_callback).grid(row=2, column=0)
        
        
    def creation_bouton_jeu_a_deux(self, label="Jeu à deux", fn_callback=None):
        self._jeu_a_deux = Bouton(self, label, fn_callback).grid(row=3, column=0)
    
    def creation_bouton_quitter(self, label="Quitter", fn_callback=None):
        self._quitter = Bouton(self, label, fn_callback).grid(row=4, column=0)
    
    
    def label_nom_du_jeu(self):
        _label_nom = Label(self, text=NOM_DU_JEU, font=("Helvetica", 25)).grid(row=0, column=0)
    
    def label_description(self):
        _label_description = Label(self, text=DESCRIPTION, font=("Helvetica", 8, "italic"), wraplength=290).grid(row=5, column=0, pady = 20)
    
    def fixer_des_options(self, *options):
        """
            Permet de fixer des options de la frame 
        """
        self.config(*options)