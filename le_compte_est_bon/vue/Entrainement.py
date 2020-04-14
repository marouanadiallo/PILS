#encoding:utf-8
from tkinter import Frame, Label
from vue.Bouton import Bouton
from datas.donnees_vue import LES_OPERATEURS

class PremiereSection(Frame):
    """
    """
    
    def __init__(self, master, valeur_n, *fn_callback):
        Frame.__init__(self, master)

        self.nouvelle_parte(fn_callback[0])
        self.valeur_N(valeur_n)
        self.bouton_solution(fn_callback[1])
        
    def bouton_solution(self, fn_callback):
        """
        """
        _b = Bouton(self, "Solution", fn_callback)
        _b.fixer_des_options(font=("Helvetica", 20), padx=5, pady=10, borderwidth=2, background="#3CB371", fg="white", activebackground="#2E8B57", activeforeground="white")
        _b.grid(row = 0, column = 3, padx = 5, pady = 5)
    
    def valeur_N(self, n):
        """
        """
        Label(self, text=n, font=("Helvetica", 20, "bold"), bd =1, relief="groove", padx = 30, pady = 20).grid(row=0, column=1, padx = 50,)
    
    def nouvelle_parte(self, fn_callback):
        """
        """
        _np = Bouton(self, "Nouvelle partie", fn_callback)
        _np.fixer_des_options(font=("Helvetica", 20), padx=2, pady=10)
        _np.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        
# ******************************************************************************************************

class SecondeSection(Frame):
    """
        Cette classe définie la première vue de la vue d'entrainement
        section des plaques, operateurs
    """
    def __init__(self, master, liste_plaques, fn_callback):
        Frame.__init__(self, master)
        self._liste_plaques = list()
        self._liste_operateurs = list()
        
        
        self.affiche_les_plaques(liste_plaques, fn_callback)
        self.affiche_les_operateurs(fn_callback)
    
    def affiche_les_plaques(self, liste_plaques, fn_callback):
        """
        """
        for i in range(0, len(liste_plaques)):
            _tmp = Bouton(self, liste_plaques[i], lambda indice = i :fn_callback(indice))
            _tmp.fixer_des_options(font=("Helvetica", 15), padx=10, pady=10)
            _tmp.grid(row = 0, column = i, padx = 5, pady =5)
            self._liste_plaques.append(_tmp)
            
    def affiche_les_operateurs(self, fn_callback):
        """
        """
        for i in range(0, len(LES_OPERATEURS)):
            _temp = Bouton(self, LES_OPERATEURS[i], lambda indice = i:fn_callback(indice))
            _temp.fixer_des_options(font=("Helvetica", 15), padx=10, pady=10)
            _temp.grid(row = 3, column = i+1, padx = 3, pady =3)
            self._liste_operateurs.append(_temp)
             
    def desactive_bouton(self, index):
        """
        """
        self._liste_plaques[index].fixer_des_options(state="disable")
    
    def mettre_à_jour_plques(self, anciennes_plaques, nouvelles_plaques):
        """
        """
        self.supp_plaques(anciennes_plaques)
        self.affiche_les_plaques(nouvelles_plaques)
        
    def supp_plaques(self, liste_plaques):
        """
        """
        for i in range(0, len(liste_plaques)):
            self._liste_plaques[i].destroy()


#**************************************************************************************************************************
class Entrainement(Frame):
    """
    """
    
    def __init__(self, master,tirage, valeur_n, fnc_callback):
        Frame.__init__(self, master)
        
        #instanciation de la deuxième section
        self._section_2 = SecondeSection(self,tirage, fnc_callback[2])
        self._section_2.grid(row = 1, column = 0, padx =5, pady = 5)
        
        #instanciation de la première section
        self._section_1 = PremiereSection(self,valeur_n, fnc_callback[0], fnc_callback[1])
        self._section_1.grid(row = 0, column = 0, padx = 5, pady = 25)
        
    
    
    def bouton_effectuer_operation(self, fn_callback):
        """
        """
        self._bouton_effectuer = Bouton(self, "Effectuer", fn_callback)
        self._bouton_effectuer.fixer_des_options(font=("Helvetica", 15), padx=5, pady=5, state="disable")
        self._bouton_effectuer.grid(row = 2, column = 0, padx = 5, pady = 5)