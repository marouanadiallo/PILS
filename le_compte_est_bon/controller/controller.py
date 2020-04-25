#encoding:utf-8
import random as rn
import re                                               #pour pouvoir utilser les expréssions régulière
from vue.vue import Vue

from modeles.Joueur import Joueur
from modeles.Plaque import Plaque
from datas.donnees_vue import INTERVALLE_DE_N
from modeles.resolution_auto import resolution_automatique


from modeles.operateurDivision import OperateurDivision
from modeles.operateurFois import OperateurFois
from modeles.operateurMoins import OperateurMoins
from modeles.operateurPlus import OperateurPlus

class Controller:
    """
    """
    
    def __init__(self):
        self._vue = Vue(self)
        
        self._operandes = list()        #stocke les opérandes choisies
        self._indices = list()          #indice des opérandes choisies
        
        self._op_select = False         #opérateur est selectionée ou non
        self._indice_op = None         #indice de l'opérateur choisie
        
        self._plaques_tirees  = self.tirage(6)
        
    def cree_joueur(self, nom):
        """
            Crée un joueur pour une partie
        """
        if re.match('^[a-zA-Z]{2,}[a-zA-Z0-9_]*', nom) == None:
            return None
        else:
            self._joueur = Joueur(nom)
            return 1
        
    def tirage(self, n):
        """
            Appelle la méthode de tirage des plaques de la classe plaque qui retourne une liste de 6 plaques
        """
        return Plaque.tirage(n)
    
    def les_plaques_tirees(self):
        """
            Retourne la liste des plaques tirées au hasard
        """
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
        
        resultat = self._joueur.effectuer_une_operation(self._operandes[0], self._operandes[1], self._indice_op)
        if resultat != None:
            self._plaques_tirees.remove(self._operandes[0])
            self._plaques_tirees.remove(self._operandes[1])
            self._plaques_tirees.append(resultat)
            
            self._vue._vue_entrainement.get_section_2().mettre_a_jour_apres_operation(resultat)              #mettre à jour les plaques utilisable
            self._vue._vue_entrainement.get_section_2().activer_tous_sauf_la_liste(self._indices)
            self._vue._vue_entrainement.get_section_3().afficher_operation(self._joueur.get_derniere_operation(), self._indice_op)
            self._vue._vue_entrainement.desactiver_bouton_effectuer()
            
            self._indices.clear()
            self._operandes.clear()
            self._op_select = False
            
            print(f"les plaques diponible après votre opération : {self._plaques_tirees}")
            self.a_gagner_ou_non(resultat)                                                                  #on vérifie s'il a trouvé la valeur N
        else:
            self.annuller_operation()
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
            self.lancer_une_alerte("Félicitation vous avez trouvé, cliquez sur ok pour une nouvelle partie !")
            self.relance_nouvelle_partie()
    
    def activer_vue_creer_joueur(self, index):
        """
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
        self._indice_op = arg
        self._op_select = True
        if len(self._indices) == 2:
            self._vue._vue_entrainement.activer_bouton_effectuer()
            
        
    def get_valeur_et_indice_plaque(self, indice, valeur):
        """
        """
        if len(self._indices) < 2:
            self._indices.append(indice)
            self._operandes.append(valeur)
            
            self._vue._vue_entrainement.get_section_2().desactiver_un_btn(indice)
            if len(self._indices) == 2:
                self._vue._vue_entrainement.get_section_2().desactiver_tous_les_btn()
                if self._op_select:
                    self._vue._vue_entrainement.activer_bouton_effectuer()
                    print(f"Les opérandes sont : {self._operandes}")
                    print(f"Les indices des opérandes choisie sont : {self._indices}")
           
                
        
    
    def relance_nouvelle_partie(self):
        """
        """
        self._plaques_tirees = self.tirage(6)
        self._vue._vue_entrainement.relance_nouvelle_partie(self.tirer_n_aleatoirement(), self._plaques_tirees)
        
        self._indices.clear()
        self._operandes.clear()
        self._op_select = False
    
    def supprimer_derniere_operation(self, listbox):
        """
        """        
        listbox.delete('end')
        op = self._joueur.supprime_derniere_operation()
        self._plaques_tirees.remove(op[-1])
        self._plaques_tirees.append(op[0])
        self._plaques_tirees.append(op[1])
        self._vue._vue_entrainement.get_section_2().mettre_a_jours_les_plaques(op[-1])
        
        les_element = listbox.get(0, 'end')
        if len(les_element) == 0:
            self._vue._vue_entrainement._section_3.desactive_btn_supp()
        print(self._plaques_tirees)
      
    def generer_solution(self):
        """
        """
        self._vue._vue_entrainement.get_section_3().vider_solution()
        
        _liste_plaque = [self._N] + self._plaques_tirees
        _liste_operations = list()
        min_difference = 1000
        nombre_plus_proche = 0
        max = 6
        #construction de la chaine de responsabilité
        _division = OperateurDivision(None)
        _fois = OperateurFois(_division)
        _moins = OperateurMoins(_fois)
        _plus = OperateurPlus(_moins)
        
        if not resolution_automatique(_liste_plaque, max,  _plus, _liste_operations, min_difference, nombre_plus_proche) :
           _liste_plaque.clear()
           _liste_plaque = [nombre_plus_proche] + self._plaques_tirees
           resolution_automatique(_liste_plaque, max,  _plus, _liste_operations, min_difference, nombre_plus_proche)
            
        for operation in _liste_operations:
            self._vue._vue_entrainement.get_section_3()._listebox_solution.insert('end', operation)
        
    
         
    def activer_vue_jeu_a_deux(self, pseudo):
        """
        """
        if self.cree_joueur(pseudo) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
            print(self._joueur.nom)
    
    
    
    def annuller_operation(self):
        """
        """
        self._vue._vue_entrainement.get_section_2().annuller_derniere_operation()
        self._vue._vue_entrainement.desactiver_bouton_effectuer()
        
        self._indices.clear()
        self._operandes.clear()
        self._op_select = False
        
    def lancer_la_vue(self):
        """
            Lance la vue
        """
        self._vue.mainloop()