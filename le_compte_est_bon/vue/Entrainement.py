#encoding:utf-8
from tkinter import Frame
from vue.Bouton import Bouton
from datas.donnees_vue import LES_OPERATEURS

class Partie_1(Frame):
    """
    """
    def __init__(self, master, liste_plaques, fn_callback):
        Frame.__init__(self, master)
        self._liste_plasues = list()
        self._liste_operateurs = list()
        
        
        self.affiche_les_plaques(liste_plaques, fn_callback)
        self.affiche_les_operateurs(fn_callback)
    
    def affiche_les_plaques(self, liste_plaques, fn_callback):
        """
        """
        for i in range(0, len(liste_plaques)):
            self._liste_plasues.append(Bouton(self, liste_plaques[i], lambda indice = i :fn_callback(indice)).grid(row = 0, column = i, padx = 3, pady =3))
            
    def affiche_les_operateurs(self, fn_callback):
        """
        """
        for i in range(0, len(LES_OPERATEURS)):
            self._liste_operateurs.append(Bouton(self, LES_OPERATEURS[i], lambda indice = i:fn_callback(indice)).grid(row = 3, column = i+1, padx = 3, pady =3))
             
    def desactive_bouton(self, index):
        """
        """
        self._liste_plasues[index].fixer_des_options(state="disable")
        
class Entrainement(Frame):
    """
    """
    
    def __init__(self, master,tirage, fnc_callback):
        Frame.__init__(self, master)
        self._partie_1 = Partie_1(self,tirage, fnc_callback)
        self._partie_1.grid(row = 0, column = 0)
        
    

