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
        self._section_2 = SectionDeux(self, self._controller)
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
        
    def activer_bouton_effectuer(self, list_non_desactive):
        """
            Cette méthode active le bouton éffectuer une opération et desactive les autres plaques non sélectionnée
        """
        self._bouton_effectuer.config(state="normal")
        self._section_2.desactive_les_plaques(list_non_desactive)
        
    def activer_les_plaques(self):
        """
            Cette méthode est appellée quand on souhaite relancé une nouvelle partie
        """
        self._section_2.activer_les_plaques_()
    
    def mise_a_jour_des_plaque(self, liste):
        """
            cette méthode est appellée à chaque oprération effectuée pour affiché la nouvelle plaque et désactivé les plaques utilisée
        """
        self._section_2.active_les_plaques_disponible()
        self._section_2.desactive_une_liste_de_plaque(liste)
        self._section_2.update_nouvelle_plaque()
        
        
    def update_btn_texts(self, plaques, n):
        """
            Cette méthode est appellée à chaque fois que le joueur souhaite refaire une nouvelle partie
            dans ce cas on modifie le text des boutons par des les nouvelles plaques ainsi que la valeur n à trouver
        """
        self._section_2.update_btn_texts(plaques)
        self._section_1.update_label_n(n)
        self.desactiver_bouton_effectuer()
        self._section_3.vider_historique()
    
    def get_value_btn(self, indice):
        """
            retourn la valeur (textvariable) d'un bouton (plaque)
        """
        return self._section_2.get_value_textvariable(indice)
    
    def affiche_operation(self, operation, indice_operation):
        """
            Appelle la méthode affiche l'opération de la section 3
        """
        self._section_3.affiche_operation(operation, indice_operation)
    def activer_une_liste_de_plaque(self, liste):
        """
        """
        self._section_2.active_une_liste_de_plaque(liste)