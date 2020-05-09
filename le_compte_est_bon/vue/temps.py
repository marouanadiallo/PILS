#encoding:utf-8

from tkinter import Frame, Entry, Label, Canvas, PhotoImage, IntVar
from vue.Bouton import Bouton
from datas.donnees_vue import PATH_CONNEXION

class DefinirTemps(Frame):
    """
    """
    
    def __init__(self, master):
        Frame.__init__(self,master)
          
    
    def champ_saisie(self):
        self._temps = IntVar()
        Entry(self, font=("Helvetica", 10), textvariable=self._temps).grid(row=2, column=0)
    
    def get_temps(self):
        """
        """
        return self._temps.get()
    
    def set_temps(self, temps):
        return self._temps.set(temps)
    
    def bouton_definir(self, label, fn_callback):
        self._creer = Bouton(self, label, fn_callback).grid(row=4, column=0)
    
    def label_champ(self):
        Label(self, text="Veuillez définir le temps:", font=("Helvetica", 20)).grid(row=0, column=0)
        
    def destructeur(self):
        """
        """
        self.destroy()