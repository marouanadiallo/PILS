#encoding:utf-8
from tkinter import Frame, Label, StringVar
from vue.Bouton import Bouton
from datetime import time

class SectionUne(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self,master)
        self._controller = controller
    
    def nouvelle_partie(self):
        """
        """
        _np = Bouton(self, "Nouvelle partie", self._controller.relance_nouvelle_partie)
        _np.fixer_des_options(font=("Helvetica", 20), padx=2, pady=5)
        _np.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    def valeur_N(self):
        """
        """
        self._n = StringVar()
        Label(self, textvariable= self._n, font=("Helvetica", 20, "bold"), bd =1, relief="groove", padx = 30, pady = 5).grid(row=0, column=1, padx = 150)
        self._n.set(self._controller.tirer_n_aleatoirement())
    
    def update_label_n(self, n):
        """
            Met à jour la nouvelle valeur à trouver 
        """
        self._n.set(n)
        
    def bouton_solution(self):
        """
        """
        _b = Bouton(self, "Solution", self._controller.generer_solution)
        _b.fixer_des_options(font=("Helvetica", 20), padx=5, pady=5, borderwidth=2, background="#3CB371", fg="white", activebackground="#2E8B57", activeforeground="white")
        _b.grid(row = 0, column = 3, padx = 5, pady = 5)
    