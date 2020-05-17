from tkinter import Frame, Menu, Label, StringVar, Entry
from vue.Bouton import Bouton
from vue.sections.sectionUne import SectionUne
from vue.sections.sectionDeux import SectionDeux
from vue.sections.sectionTrois import SectionTrois

class VueManager(Frame):
    
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self._controller = controller
        
        self.text_p = StringVar()
        self.text_s = StringVar()
        
        self._section_2 = SectionDeux(self, self._controller)
        self._section_1 = SectionUne(self,self._controller) 
        self._section_3 = SectionTrois(self, self._controller)
        
        
        #Ajout d'un menu 
        menubar = Menu(master)
        optionmenu = Menu(menubar, tearoff = 0)
        
        optionmenu.add_separator()
       
        optionmenu.add_command(label="Retour accueil", command = self._controller.retourner_accueil)
        optionmenu.add_separator()
        optionmenu.add_command(label = "Quitter", command = master.quit)
        menubar.add_cascade(label = "Options", menu = optionmenu)
        
        
        aproposmenu = Menu(menubar, tearoff=0)
        aproposmenu.add_command(label = "Description", command = self.description_entrainement)
        menubar.add_cascade(label = "A propos", menu = aproposmenu)

        
        master.config(menu = menubar)               #ajout du menu
    
    @property
    def section_2(self):
        return self._section_2
    
    @property
    def section_1(self):
        return self._section_1
    
    @property
    def section_3(self):
        return self._section_3
     
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
        self._section_3.vider_solution()
        self.desactiver_bouton_effectuer()
    
    def activer_vue_entrainement(self):
        self.section_2.affiche_les_plaques(self._controller.les_plaques_tirees())
        self.section_2.affiche_les_operateurs()
        self.section_2.grid(row = 1, column = 0,  padx =5, pady = 5)
        
        self.section_1.nouvelle_partie()
        self.section_1.valeur_N(self._controller.tirer_n_aleatoirement())
        self.section_1.bouton_solution()
        self.section_1.grid(row = 0, column = 0, padx = 5, pady = 10)
        
        self.section_3.grid(row = 3, column =0)
        
        self.bouton_effectuer_operation()
        
    def activer_vue_jeu_a_deux_part_1(self, temps, n):
        
        self._temps = self.section_1.label_compte_a_rebours(temps)
        self.section_1.valeur_N(n)
        self.section_1.bouton_stop()
        
        self.section_1.grid(row = 0, column = 0, padx = 5, pady = 10)
        
        self.update_profil(self._controller._joueur.nom)
        self.update_score(0)
        self.profil_joueur()
        self._profil.grid(row = 4, column = 0, pady = 5)
        self._score.grid(row = 5, column = 0, pady = 5)
        
    def activer_vue_jeu_a_deux_part_2(self, plaques):
        
        self.section_2.affiche_les_plaques(plaques)
        self.section_2.affiche_les_operateurs()
        self.section_2.grid(row = 1, column = 0,  padx =5, pady = 5)
        
        self.bouton_effectuer_operation()
        
    def veuillez_patienter(self):
        self._vp = Label(self, text="En attente du deuxième joueur, veuillez patienter s'il vous plaît, merci !", font=("Helvetica", 20)) 
        self._vp.pack(pady=300)
        
    def supprimer_vp(self):
        self._vp.pack_forget()
        
    def description_entrainement(self):
        """
        """
        pass
    
    def profil_joueur(self):
        """
        """
        self._profil = Label(self, text= self.text_p.get(), font=("Helvetica", 15))
        self._score =  Label(self, text= self.text_s.get(), font=("Helvetica", 15))
    
    def update_profil(self, pseudo):
        self.text_p.set("Profil :" + pseudo)
    
    def update_score(self, score):
        self.text_s.set("Score :" + str(score))
    
    def nombre_trouver(self):
        self._nb_trouver = StringVar()
        Label(self, text="Quel nombre avez-vous trouvé ? ", font=("Helvetica", 15)).grid(row = 6, column = 0, padx = 5, pady = 5)
        self._champ_nb_trouver = Entry(self, textvariable = self._nb_trouver).grid(row = 7, column = 0, padx = 5, pady = 5)
    
    def get_nb_trouver(self):
        return self._nb_trouver.get()
    
    def btn_nb_trouver(self):
        self._btn_nb_trouver = Bouton(self, "Envoyer", lambda:self._controller.agent_nb_trouver(self.get_nb_trouver()))
        self._btn_nb_trouver.fixer_des_options(font=("Helvetica", 10), padx=10, pady=5)
        self._btn_nb_trouver.grid(row = 8, column = 0, padx = 5, pady = 5)
        
    def afficher_aprs_stop(self):
        """
        """
        self._label_trouver = Label(self, text="Votre adversaire s'annonce avoir trouver, veuillez patienter svp !", font=("Helvetica", 15)).grid(row = 3, column = 0, pady = 20)
        
    def supprimer_trouver(self):
        self._label_trouver.grid_forget()
        