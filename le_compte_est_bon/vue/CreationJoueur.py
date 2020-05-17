#encoding:utf-8

from tkinter import Frame, Entry, Label, Canvas, PhotoImage, StringVar
from vue.Bouton import Bouton
from datas.donnees_vue import PATH_CONNEXION

class CreationJoueur(Frame):
    """
    """
    
    def __init__(self, master):
        Frame.__init__(self,master)
        
        self.label_champ()
        self.champ_saisie()
        
    
    def champ_saisie(self):
        self._pseudo = StringVar()
        Entry(self, font=("Helvetica", 10), textvariable=self._pseudo).grid(row=2, column=0)
    
    def bouton_creer(self, label, fn_callback):
        self._creer = Bouton(self, label, fn_callback)
        self._creer.fixer_des_options(font=("Helvetica", 10), padx=10, pady=5)
        self._creer.grid(row=4, column=0)
    
    def label_champ(self):
        Label(self, text="Veuillez saisir un pseudo s'il vous plaît :", font=("Helvetica", 15)).grid(row=0, column=0)