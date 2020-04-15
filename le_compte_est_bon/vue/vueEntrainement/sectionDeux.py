from tkinter import Frame, StringVar, Button
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
        
        self._liste_textvar = list()
        
        self._plaques_tirees = self._controller.tirage()
        self.affiche_les_plaques(self._plaques_tirees)
        self.affiche_les_operateurs()
    
    

    def get_value_textvariable(self, index):
        """
        """
        return int(self._liste_textvar[index].get())
    
    def update_btn_texts(self, plaques):
        """
        """
        self._plaques_tirees = plaques  #mettre à jour la liste des plaque
        for i in range(0,len(plaques)):
            self._liste_textvar[i].set(plaques[i])
            
        for i in range(len(plaques), len(self._liste_textvar)-1):
            self._liste_textvar[i].set("_")
            self.desactive_bouton(i)
            
    def update_nouvelle_plaque(self):
        """
            cette méthode affiche la valeur de la dernière opération sur le premier bouton de label _ trouvé et l'active également
        """
        for i in range(6, 11):
            if self._liste_textvar[i].get() == "_":
                self._liste_textvar[i].set(self._plaques_tirees[-1])
                self.activer_une_plaque(i)
                break
        
    
    def affiche_les_plaques(self, plaques):
        """
        """
        j = 0
        for i in range(0, len(plaques)*2):
            self._liste_textvar.append(StringVar())
            _tmp = Button(self, textvariable = self._liste_textvar[i] , command=lambda indice = i :self._controller.get_value_plaque(indice))
            _tmp.config(font=("Helvetica", 15), padx=5, pady=2)
            if i < len(plaques): 
                self._liste_textvar[i].set(plaques[i]) 
                _tmp.grid(row = 0, column = i, padx = 5, pady = 3)
            else: 
                if i == (len(plaques)*2)-1:
                    self._liste_textvar[i].set("C")
                    _tmp.config(command = self._controller.annuller_operation)
                else:
                    self._liste_textvar[i].set("_")
                    _tmp.config(state='disable')
                _tmp.grid(row = 1, column = j, padx = 5, pady = 3)
                j = j+1
            
            self._liste_plaques.append(_tmp)
            
    def affiche_les_operateurs(self):
        """
        """
        for i in range(0, len(LES_OPERATEURS)):
            _temp = Bouton(self, LES_OPERATEURS[i], lambda indice = i:self._controller.get_indice_operateur(indice))
            _temp.fixer_des_options(font=("Helvetica", 15), padx=5, pady=3)
            _temp.grid(row = 2, column = i+1, padx = 3, pady =3)
            self._liste_operateurs.append(_temp)
    
    def desactive_bouton(self, index):
        """
        """
        self._liste_plaques[index].config(state="disable")
        
    def desactive_les_plaques(self, non_desactive):
        """
        """
        for i in range(0,len(self._liste_plaques)-1):
            if i not in non_desactive:
                self.desactive_bouton(i)
                
    def desactive_une_liste_de_plaque(self, liste):
        """
            Cette méthode desactive la liste d'indice passé en paramètre
        """
        for i in range(0, len(liste)):
            self.desactive_bouton(liste[i])
                
    def activer_une_plaque(self, index):
        """
        """
        self._liste_plaques[index].config(state="normal")
        
    def activer_les_plaques_(self):
        """
            Cette méthode est appellée quand on souhaite relancé une nouvelle partie
        """
        for i in range(0,len(self._liste_plaques)-1):
            if self._liste_textvar[i].get() != "_":
                self.activer_une_plaque(i)
                
    def active_les_plaques_disponible(self):
        """
        """
        for i in range(0,len(self._liste_plaques)-1):
            if self._liste_textvar[i].get() != "_" and int(self._liste_textvar[i].get()) in self._plaques_tirees[0:len(self._plaques_tirees)-1]:
                self.activer_une_plaque(i)
                
    def active_une_liste_de_plaque(self, liste):
        """
            Active une liste de paque donnée (opération supprimé)
        """
        for i in range(0,len(self._liste_plaques)-1):
            if self._liste_textvar[i].get() != "_" and int(self._liste_textvar[i].get()) in [liste[0], liste[1]]:
                self.activer_une_plaque(i)
            elif self._liste_textvar[i].get() != "_" and int(self._liste_textvar[i].get()) == liste[-1]:
                self._liste_textvar[i].set("_")
                self.desactive_bouton(i)
    
    def annuller_op(self, liste):
        """
        """
        for i in range(0,len(self._liste_plaques)-1):
            if self._liste_textvar[i].get() != "_" and int(self._liste_textvar[i].get()) in liste:
                self.activer_une_plaque(i)