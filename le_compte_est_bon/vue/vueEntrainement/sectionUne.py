#encoding:utf-8
from tkinter import Frame, Label
from vue.Bouton import Bouton

class SectionUne(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self,master)
        self._controller = controller
        
        self.nouvelle_partie()
        self.valeur_N()
        self.bouton_solution()
    
    def nouvelle_partie(self):
        """
        """
        _np = Bouton(self, "Nouvelle partie", self._controller.relance_nouvelle_partie)
        _np.fixer_des_options(font=("Helvetica", 20), padx=2, pady=10)
        _np.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    def valeur_N(self):
        """
        """
        Label(self, text=self._controller.tirer_n_aleatoirement(), font=("Helvetica", 20, "bold"), bd =1, relief="groove", padx = 30, pady = 20).grid(row=0, column=1, padx = 50,)
    
    def bouton_solution(self):
        """
        """
        _b = Bouton(self, "Solution", self._controller.generer_solution)
        _b.fixer_des_options(font=("Helvetica", 20), padx=5, pady=10, borderwidth=2, background="#3CB371", fg="white", activebackground="#2E8B57", activeforeground="white")
        _b.grid(row = 0, column = 3, padx = 5, pady = 5)
    