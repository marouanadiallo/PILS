#encoding:utf-8

from tkinter import Frame, Entry, Label, Canvas, PhotoImage, StringVar
from vue.Bouton import Bouton
from datas.donnees_vue import PATH_CONNEXION

class DefinirTemps(Frame):
    """
    """
    
    def __init__(self, master):
        Frame.__init__(self,master)
          
    
    def champ_saisie(self):
        self._temps = StringVar()
        Entry(self, font=("Helvetica", 10), textvariable=self._temps).grid(row=2, column=0)
    
    def get_temps(self):
        """
        """
        if len(self._temps.get()) == 0:
            self._temps = 45
            return self._temps
        else:
            return self._temps
        
    
    def set_temps(self, temps):
        return self._temps.set(temps)
    
    def bouton_definir(self, label, fn_callback):
        self._creer = Bouton(self, label, fn_callback)
        self._creer.fixer_des_options(font=("Helvetica", 10), padx=10, pady=5)
        self._creer.grid(row=4, column=0)
    
    def label_champ(self):
        Label(self, text="Veuillez définir le temps (Par defaut le temps est définie à 45 secondes):", font=("Helvetica", 15)).grid(row=0, column=0)
        
    def destructeur(self):
        """
        """
        self.destroy()