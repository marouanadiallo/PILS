from tkinter import Frame, StringVar, Button, Label
from vue.Bouton import Bouton
from datas.donnees_vue import LES_OPERATEURS

class SectionDeux(Frame):
    """
    """
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        
        self._liste_btn_plaques = list()
        self._liste_btn_operateurs = list()
        
        self._liste_textvar = list()
        self._list_btn_desactive = list()
    

    def affiche_les_plaques(self, plaques):
        """
        """
        j = 0
        for i in range(0, len(plaques)*2):
            self._liste_textvar.append(StringVar())
            _tmp = Button(self, textvariable = self._liste_textvar[i] , command=lambda indice = i:self._controller.get_valeur_et_indice_plaque(indice, int(self.get_valeur_btn(indice))))
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
            
            self._liste_btn_plaques.append(_tmp)
            
    def get_valeur_btn(self, indice):
        """
            Renvoie la valeur associée au bouton de l'indice passé en paramètre
        """ 
        return self._liste_textvar[indice].get()
           
    def changer_les_plaques(self, plaques):
        """
            Cette méthode met à jour les plaques selon la liste des plaques passé en paramètre
        """
        self._list_btn_desactive.clear()
        for i in range(0, len(plaques)):
            self._liste_textvar[i].set(plaques[i])
            if self._liste_btn_plaques[i]["state"] == "disabled":
                self.activer_un_btn(i)
                
        for j in range(len(self._liste_textvar)//2, len(self._liste_textvar)-1):
            self._liste_textvar[j].set("_")
            self.desactiver_un_btn(j)
        print("***************************************************************")
        print(f"Nouvelle tirage : {plaques}")
    
    def mettre_a_jour_apres_operation(self, resultat):
        """
            Ajoute la plaque resultante d'une opération
        """
        for i in range(len(self._liste_textvar)//2, len(self._liste_textvar)-1):
            if self.get_valeur_btn(i) == "_":
                self._liste_textvar[i].set(resultat)
                self.activer_un_btn(i)
                break
                
    def annuller_derniere_operation(self):
        """
        """                   
        for j in range(0, len(self._liste_btn_plaques)-1):
            if j not in self._list_btn_desactive and self._liste_textvar[j].get() != "_":
                self.activer_un_btn(j)
                
    def mettre_a_jours_les_plaques(self, resultat):
        """
            Active les plaques de la dernière opération supprimée
        """
        self.activer_un_btn(self._list_btn_desactive.pop())
        self.activer_un_btn(self._list_btn_desactive.pop()) 

        last_index = 0
        
        for i in range(0, len(self._liste_textvar)-1):
            if self._liste_textvar[i].get() != "_" and int(self._liste_textvar[i].get()) == resultat:
                #On garde dans une variable l'indice du dernier nombre à supprimer
                last_index = i

        #On le supprime ici
        self._liste_textvar[last_index].set("_")
        self.desactiver_un_btn(last_index)
                
    def desactiver_tous_les_btn(self):
        """
            cette méthode désactive tous les bouton sauf le bouton C (annulé les plaques choisie)
        """
        for i in range(0, len(self._liste_btn_plaques)-1):
             if self._liste_btn_plaques[i]["state"] == "normal":
                self.desactiver_un_btn(i)
    
    
    def desactiver_un_btn(self, indice):
        """
            Désactive le bouton d'indice passé en param
        """
        self._liste_btn_plaques[indice].config(state="disabled")
        
    def activer_un_btn(self, indice):
        """
            Active le bouton d'indice passé en param
        """
        self._liste_btn_plaques[indice].config(state="normal")
        
    def activer_tous_sauf_la_liste(self, liste_indice):
        """
            Cette méthode active les plaques utilisable 
        """
        self._list_btn_desactive.extend(liste_indice)
        for i in range(0, len(self._liste_btn_plaques)-1):
            if i not in self._list_btn_desactive and self._liste_textvar[i].get() != "_":
                self.activer_un_btn(i)
                
    def affiche_les_operateurs(self):
        """
        """
        for i in range(0, len(LES_OPERATEURS)):
            _temp = Bouton(self, LES_OPERATEURS[i], lambda indice = i:self._controller.get_indice_operateur(indice))
            _temp.fixer_des_options(font=("Helvetica", 15), padx=5, pady=3)
            _temp.grid(row = 2, column = i+1, padx = 3, pady = 3)
            self._liste_btn_operateurs.append(_temp)
            
    