#encoding:utf-8
from tkinter import Frame
from vue.Bouton import Bouton
from vue.vueEntrainement.sectionUne import SectionUne
from vue.vueEntrainement.sectionDeux import SectionDeux
from vue.vueEntrainement.sectionTrois import SectionTrois

class Entrainement(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        
        #instanciation de la deuxième section
        self._section_2 = SectionDeux(self, self._controller, self._controller.les_plaques_tirees())
        self._section_2.grid(row = 1, column = 0,  padx =5, pady = 5)
        
        #instanciation de la première section
        self._section_1 = SectionUne(self,self._controller)
        self._section_1.grid(row = 0, column = 0, padx = 5, pady = 10)
        
        #instanciation de la section print solution
        self._section_3 = SectionTrois(self, self._controller)
        self._section_3.grid(row = 3, column =0)
        
        self.bouton_effectuer_operation()
        
    
    
    def bouton_effectuer_operation(self):
        """
        """
        self._bouton_effectuer = Bouton(self, "Effectuer", self._controller.effectuer_une_operation)
        self._bouton_effectuer.fixer_des_options(font=("Helvetica", 15), padx=43, pady=5, state="disabled")
        self._bouton_effectuer.grid(row = 2, column = 0, padx = 5, pady = 5)
    
    def desactiver_bouton_effectuer(self):
        """
        """
        self._bouton_effectuer.fixer_des_options(state="disabled")
    
    def activer_bouton_effectuer(self):
        """
        """
        self._bouton_effectuer.fixer_des_options(state="normal")   
        
    def relance_nouvelle_partie(self, nouveau_n, nouvelle_liste):
        """
        """
        self._section_1.update_label_n(nouveau_n)                       #mettre la valeur à trouver à jour
        self._section_2.changer_les_plaques(nouvelle_liste)             #met à jour les plaques
        self._section_3.vider_historique()                              #efface l'historique
        self.desactiver_bouton_effectuer()
        
    def get_section_2(self):
        return self._section_2
    
    def get_section_1(self):
        return self._section_1
    
    def get_section_3(self):
        return self._section_3