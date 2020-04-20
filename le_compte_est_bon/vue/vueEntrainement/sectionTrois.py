#encoding:utf-8

from tkinter import Frame, Listbox, Label, Scrollbar
from vue.Bouton import Bouton
from datas.donnees_vue import LES_OPERATEURS

class SectionTrois(Frame):
    """
    """
    
    def __init__(self, master,  controller):
        Frame.__init__(self, master)
        self._controller = controller
        
        self.labels_()
        self.liste_box_()
        self.btn_supp_derniere_opetation()
    
    def labels_(self):
        """
        """
        self._label = Label(self, text="Historique de vos opérations", font=("Helvetica", 10, "bold"), pady = 2)
        self._label.grid(row = 0, column = 0, padx = 130, pady=5)
        
        self._label_s = Label(self, text="Cliquez sur le bouton solution pour voir la resolution de cette partie !", font=("Helvetica", 10, "bold"), wraplength = 200, pady = 2)
        self._label_s.grid(row = 0, column = 1, padx = 130, pady=5)
        
    def liste_box_(self):
        """
        """        
        self._listebox_historique = Listbox(self, bd =2 , relief="groove", width=50, font=("Helvetica", 10, "bold"))
        self._listebox_historique.grid(row = 1, column = 0, pady = 2)
        
        self._listebox_solution = Listbox(self, bd =2 , relief="groove", state="disabled", width=50, font=("Helvetica", 10, "bold"))
        self._listebox_solution.grid(row = 1, column=1, pady = 2)
    
    def btn_supp_derniere_opetation(self):
        """
        """
        self._btn = Bouton(self, "SUPP derniere opération", lambda: self._controller.supprimer_derniere_operation(self._listebox_historique))
        self._btn.fixer_des_options(font=("Helvetica", 15), state="disabled", padx=2, pady=5)
        self._btn.grid(row = 2, column = 0, pady = 5)
        
    def activer_btn_supp(self):
        """
        """
        self._btn.fixer_des_options(state="normal")
    
    def desactive_btn_supp(self):
        """
        """
        self._btn.fixer_des_options(state="disabled")
        
        
    def afficher_operation(self, operation, indice_operateur):
        """
            Affiche l'operation réçue en paramètre
        """
        if self._btn["state"] == "disabled":
            self.activer_btn_supp()
            
        if indice_operateur == 1:
            if operation[0] >= operation[1]:
                self._listebox_historique.insert('end', [operation[0], LES_OPERATEURS[1], operation[1], "=", operation[2]])
            else:
                self._listebox_historique.insert('end', [operation[1], LES_OPERATEURS[1], operation[0], "=", operation[2]])
        elif indice_operateur == 3:
            if operation[0] % operation[1] ==0:
                self._listebox_historique.insert('end', [operation[0], LES_OPERATEURS[3], operation[1], "=", operation[2]])
            else:
                self._listebox_historique.insert('end', [operation[1], LES_OPERATEURS[3], operation[0], "=", operation[2]])
        else:
            self._listebox_historique.insert('end', [operation[0], LES_OPERATEURS[indice_operateur], operation[1], "=", operation[2]])
    
    
    def vider_historique(self):
        """
        """
        self._listebox_historique.delete(0, 'end')