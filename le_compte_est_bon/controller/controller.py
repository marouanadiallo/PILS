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
    
    def effectuer_une_operation(self, operande_1, operande_2, index_operateur):
        """
            Cette fonction est la fonction callback du button 'effectuer' après le choix des opérandes et l'opérateur
        """
        resultat = self._joueur.effectuer_une_operation(operande_1, operande_2, index_operateur)
        if resultat != None:
            self._plaques_tirees.remove(operande_1).remove(operande_2)
            self._plaques_tirees.append(resultat)
            
            self.a_gagner_ou_non(resultat)                          #on vérifie s'il a trouvé la valeur N
            self.mettre_a_jour_les_plaques(self._plaques_tirees)    #appelle de mise à jour de la vue
        else:
            self.lancer_une_alerte("L'opération que vous souhaitez éffectuer est non permise!")
    
    def mettre_a_jour_les_plaques(self, plaques):
        """
            Cette méthode appelle la méthode mettre_a_jour_vue_des_plaques de la vue afin 
            de mettre à jour après une opération effectuée
        """
        self._vue.mettre_a_jour_vue_des_plaques(plaques)
    
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
        print("dans la vue d'entrainement,pseudo saisie : {}".format(value_champ))
        if self.cree_joueur(value_champ) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
            self._vue.vue_entrainement(self.tirage(), self.get_indice_bouton)
           
    def get_indice_bouton(self, arg):
        """
        """
        print(arg)
           
    def activer_vue_jeu_a_deux(self, value_champ):
        """
        """
        print("dans la vue jeu à deux, pseudo saisie : {}".format(value_champ))
        if self.cree_joueur(value_champ) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
            
    def lancer_la_vue(self):
        """
            Lance la vue
        """
        self._vue.mainloop()