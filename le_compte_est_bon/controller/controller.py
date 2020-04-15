#encoding:utf-8
import random as rn
import re                                               #pour pouvoir utilser les expréssions régulière
from vue.vue import Vue
from modeles.Joueur import Joueur
from modeles.Plaque import Plaque
from datas.donnees_vue import INTERVALLE_DE_N

class Controller:
    """
    """
    
    def __init__(self):
        self._vue = Vue(self)
        
        self._operandes = list()
        self._indices = list()
        
        self._op_select = False
        self._indices_op = None
        
    def cree_joueur(self, nom):
        """
            Crée un joueur pour une partie
        """
        if re.match('^[a-zA-Z]{2,}[a-zA-Z0-9_]*', nom) == None:
            return None
        else:
            self._joueur = Joueur(nom)
            return 1
        
    def tirage(self):
        """
            Appelle la méthode de tirage des plaques de la classe plaque qui retourne une liste de 6 plaques
        """
        self._plaques_tirees = Plaque.tirage()
        return self._plaques_tirees
    
    
    def tirer_n_aleatoirement(self):
        """
            tire et retourne une valeur aléatoirement entre [999 à 1000]
        """
        self._N = rn.randint(INTERVALLE_DE_N[0], INTERVALLE_DE_N[1])
        return self._N
    
    def effectuer_une_operation(self):
        """
            Cette fonction est la fonction callback du button 'effectuer' après le choix des opérandes et l'opérateur
        """
        
        resultat = self._joueur.effectuer_une_operation(self._operandes[0], self._operandes[1], self._indices_op)
        if resultat != None:
            self._plaques_tirees.remove(self._operandes[0])
            self._plaques_tirees.remove(self._operandes[1])
            self._plaques_tirees.append(resultat)
            
            self._vue._vue_entrainement.mise_a_jour_des_plaque(self._indices)           #mettre à jour les plaques utilisable
            self._vue._vue_entrainement.desactiver_bouton_effectuer()
            
            #affiche au console pour voire les opérations éffectuées
            print(f"Les plaque choisie sont : {self._operandes} et l'indice de l'opérateur choisie {self._indices_op}")
            print(f"Liste des plaques disponible après l'opération : {self._plaques_tirees}")
            
            self._vue._vue_entrainement.affiche_operation(self._joueur.get_dernier_operation(), self._indices_op)        #on affiche l'opération effectuée
            self._operandes.clear()
            self._indices.clear()
            
            self._op_select = False
            
            self.a_gagner_ou_non(resultat)                                              #on vérifie s'il a trouvé la valeur N
        else:
            self.lancer_une_alerte("L'opération que vous souhaitez éffectuer est non permise, changé d'opérateur ou cliqué sur C pour changer de plaques ! ")
        
        
        
    def lancer_une_alerte(self, msg):
        """
            Demande à la vue de lancer une alerte en affichant le message msg
        """
        self._vue.lance_alerte(msg)
    
    def a_gagner_ou_non(self, resultat):
        """
            Vérifie à chaque opération éffectuée si le joueur à trouver la la valeur N ou non
            si oui on incrément son score d'un sinon il peut continuer
        """
        if resultat == self._N:
            self.lancer_une_alerte("Félicitation vous avez trouvé !")
            self._joueur.score(1)
    
    def activer_vue_creer_joueur(self, index):
        """tirage, fnc_callback
            Cette méthode active la vue de creation d'un joueur
        """
        self._vue.cacher_vue_accueil()
        if index == 1:
            self._vue.vue_creer_joueur(self.activer_vue_entrainement)
        else:
            self._vue.vue_creer_joueur(self.activer_vue_jeu_a_deux)
    
    def activer_vue_entrainement(self, value_champ):
        """
            Cette méthode active la vue d'entrainement
        """
        if self.cree_joueur(value_champ) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
            self._vue.vue_entrainement()
            print(f"Les plaques tirées sont : {self._plaques_tirees}")
        
        
    def get_indice_operateur(self, arg):
        """
        """
        self._indices_op = arg
        if not self._op_select and len(self._indices) == 2:
            self._vue._vue_entrainement.activer_bouton_effectuer(self._indices)
            self._op_select = True
        print(self._indices_op)
        
    def get_value_plaque(self, arg):
        """
        """
        if len(self._indices) < 2:
            self._indices.append(arg)
            self._vue._vue_entrainement._section_2.desactive_bouton(arg)
            self._operandes.append(self._vue._vue_entrainement.get_value_btn(arg))  
            if not self._op_select and len(self._indices) == 2:
                self._vue._vue_entrainement.activer_bouton_effectuer(self._indices)
        print(self._operandes)
    
    def relance_nouvelle_partie(self):
        """
        """
        self._vue._vue_entrainement.update_btn_texts(self.tirage(), self.tirer_n_aleatoirement())
        self._vue._vue_entrainement.activer_les_plaques()
        
        self._indices.clear()
        self._operandes.clear()
        self._op_select = False
        
        print(f"Les plaques tirées pour une nouvelle partie sont : {self._plaques_tirees}")
    
    def supprimer_derniere_operation(self, listbox):
        """
        """            
        listbox.delete('end')
        op = self._joueur.supprime_derniere_operation()
        self._plaques_tirees.remove(op[-1])
        self._plaques_tirees.append(op[0])
        self._plaques_tirees.append(op[1])
        self._vue._vue_entrainement.activer_une_liste_de_plaque(op)
        
        les_element = listbox.get(0, 'end')
        if len(les_element) ==0:
            self._vue._vue_entrainement._section_3.desactive_btn_supp()
        print(self._plaques_tirees)
        
    def generer_solution(self):
        """
        """
        print("générer une solution")
    
         
    def activer_vue_jeu_a_deux(self, value_champ):
        """
        """
        print("dans la vue jeu à deux, pseudo saisie : {}".format(value_champ))
        if self.cree_joueur(value_champ) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
    
    def annuller_operation(self):
        """
        """
        self._vue._vue_entrainement._section_2.annuller_op(self._plaques_tirees)
        self._operandes.clear()
        self._indices.clear()
        
    def lancer_la_vue(self):
        """
            Lance la vue
        """
        self._vue.mainloop()