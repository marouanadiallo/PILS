from tkinter import Frame
from vue.Bouton import Bouton
from datas.donnees_vue import LES_OPERATEURS

class SectionDeux(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        self._liste_plaques = list()
        self._liste_operateurs = list()
        
        self.affiche_les_plaques()
        self.affiche_les_operateurs()
    
    
    
    def affiche_les_plaques(self):
        """
        """
        _les_plaque = self._controller.tirage()
        for i in range(0, len(_les_plaque)):
            _tmp = Bouton(self, _les_plaque[i], lambda indice = i :self._controller.get_indice_plaque(indice))
            _tmp.fixer_des_options(font=("Helvetica", 15), padx=10, pady=10)
            _tmp.grid(row = 0, column = i, padx = 5, pady =5)
            self._liste_plaques.append(_tmp)
            
    def affiche_les_operateurs(self):
        """
        """
        for i in range(0, len(LES_OPERATEURS)):
            _temp = Bouton(self, LES_OPERATEURS[i], lambda indice = i:self._controller.get_indice_operateur(indice))
            _temp.fixer_des_options(font=("Helvetica", 15), padx=10, pady=10)
            _temp.grid(row = 3, column = i+1, padx = 3, pady =3)
            self._liste_operateurs.append(_temp)
    
    def desactive_bouton(self, index):
        """
        """
        self._liste_plaques[index].fixer_des_options(state="disable")