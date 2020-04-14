#encoding:utf-8
from tkinter import Frame
from vue.Bouton import Bouton
from vue.vueEntrainement.sectionUne import SectionUne
from vue.vueEntrainement.sectionDeux import SectionDeux

class Entrainement(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        
        #instanciation de la deuxième section
        self._section_2 = SectionDeux(self, self._controller)
        self._section_2.grid(row = 1, column = 0, padx =5, pady = 5)
        
        #instanciation de la première section
        self._section_1 = SectionUne(self,self._controller)
        self._section_1.grid(row = 0, column = 0, padx = 5, pady = 25)
        
        self.bouton_effectuer_operation()
        
    
    
    def bouton_effectuer_operation(self):
        """
        """
        self._bouton_effectuer = Bouton(self, "Effectuer", self._controller)
        self._bouton_effectuer.fixer_des_options(font=("Helvetica", 15), padx=5, pady=5, state="disable")
        self._bouton_effectuer.grid(row = 2, column = 0, padx = 5, pady = 5)