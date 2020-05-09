#encoding:utf-8
from tkinter import Frame
from vue.vueEntrainement.sectionUne import SectionUne

class JeuADeux(Frame):
    """
    """
    def __init__(self, master, controller, temps = 45):
        Frame.__init__(self, master)
        self._temps = temps
        
        self._controller =  controller
        #instanciation de la première section
        self._section_1 = SectionUne(self,self._controller)
        self._section_1.label_compte_a_rebours(self._temps)
        self._section_1.valeur_N(self._controller.tirer_n_aleatoirement())
        self._section_1.bouton_stop()
        self._section_1.grid(row = 0, column = 0, padx = 5, pady = 10)
    