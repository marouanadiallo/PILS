#encoding:utf-8
import random as rn
import re                                               #pour pouvoir utilser les expréssions régulière
from vue.vue import Vue

from modeles.Joueur import Joueur
from modeles.Plaque import Plaque
from datas.donnees_vue import INTERVALLE_DE_N
from modeles.resolution_auto import Resolution

from modeles.operateurDivision import OperateurDivision
from modeles.operateurFois import OperateurFois
from modeles.operateurMoins import OperateurMoins
from modeles.operateurPlus import OperateurPlus

from ivy.std_api import *

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
            
            self._vue.vue_manager.section_2.mettre_a_jour_apres_operation(resultat)              #mettre à jour les plaques utilisable
            self._vue.vue_manager.section_2.activer_tous_sauf_la_liste(self._indices)
            self._vue.vue_manager.section_3.afficher_operation(self._joueur.get_derniere_operation(), self._indice_op)
            self._vue.vue_manager.desactiver_bouton_effectuer()
            
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
            self._vue.activer_vue_creer_joueur(self.activer_vue_entrainement)
        else:
            self._vue.activer_vue_creer_joueur(self.creer_agent_jeu_a_deux)
            
    
    def activer_vue_entrainement(self, value_champ):
        """
            Cette méthode active la vue d'entrainement
        """
        if self.cree_joueur(value_champ) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self._vue.cacher_vue_creer_joueur()
            self._vue.vue_manager.activer_vue_entrainement()
            self._vue.activer_vue_manager()
            print(f"Les plaques tirées sont : {self._plaques_tirees}")
        
        
    def get_indice_operateur(self, arg):
        """
        """
        self._indice_op = arg
        self._op_select = True
        if len(self._indices) == 2:
            self._vue.vue_manager.activer_bouton_effectuer()
            
        
    def get_valeur_et_indice_plaque(self, indice, valeur):
        """
        """
        if len(self._indices) < 2:
            self._indices.append(indice)
            self._operandes.append(valeur)
            
            self._vue.vue_manager.section_2.desactiver_un_btn(indice)
            if len(self._indices) == 2:
                self._vue.vue_manager.section_2.desactiver_tous_les_btn()
                if self._op_select:
                    self._vue.vue_manager.activer_bouton_effectuer()
                    print(f"Les opérandes sont : {self._operandes}")
                    print(f"Les indices des opérandes choisie sont : {self._indices}")
           
                
        
    
    def relance_nouvelle_partie(self):
        """
        """
        self._plaques_tirees = self.tirage(6)
        self._vue.vue_manager.relance_nouvelle_partie(self.tirer_n_aleatoirement(), self._plaques_tirees)
        
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
        self._vue.vue_manager.section_2.mettre_a_jours_les_plaques(op[-1])
        
        les_element = listbox.get(0, 'end')
        if len(les_element) == 0:
            self._vue.vue_manager.section_3.desactive_btn_supp()
        print(self._plaques_tirees)
      
    def generer_solution(self):
        """
        """
        self._vue.vue_manager.section_3.vider_solution()
        
        _liste_plaque = [self._N] + self._plaques_tirees
        
        resolution = Resolution()

        max = 6
        #construction de la chaine de responsabilité
        _division = OperateurDivision(None)
        _fois = OperateurFois(_division)
        _moins = OperateurMoins(_fois)
        _plus = OperateurPlus(_moins)
        
        if not resolution.resolution_automatique(_liste_plaque, max,  _plus) :
            #Il faut absolument update le nombre le plus proche pour le réutiliser ensuite
           print("On update le nombre le plus proche : " + str(resolution._nombre_plus_proche))
           _liste_plaque.clear()
           _liste_plaque = [resolution._nombre_plus_proche] + self._plaques_tirees
           resolution.resolution_automatique(_liste_plaque, max,  _plus)
            
        for operation in resolution._liste_operations:
            self._vue.vue_manager.section_3._listebox_solution.insert('end', operation)
            
    ###################################################################################################################      
        """
            IVY
        """
    ###################################################################################################################
    
            
    def definir_temps(self, temps):
        try:
            self._temps = int(temps)
            self._N = self.tirer_n_aleatoirement()
            self._vue.supp_definir_temps()
            self._vue.activer_vue_manager()
            self._vue.vue_manager.veuillez_patienter()
        except:
            self.lancer_une_alerte("Donnez un nombre SVP !")
         
    def on_die(self, *arg):
        print(f"L'ordre de terminaison de l'agent {arg[0]} de l'identifiant {str(arg[1])}")
        IvyStop()

    def get_msg(self, *args):
        
        print(f"{args[0]} a envoyé {str(args[1])}, taille : {len(args[1])}")
        self._vue.activer_vue_manager()
        
        if args[1] == "trouver":
            self._vue.vue_manager.afficher_aprs_stop()
            self._vue.vue_manager.section_1.desactiver_btn_stop()
            self._vue.vue_manager.section_1.stop_compte_a_rebours()
        else:
            lis = args[1].replace("]", "").replace("[", "").split(",")
            
            if(len(lis) == 2 and lis[0] != "nb:"):
                self._N = int(lis[1])
                self._vue.vue_manager.activer_vue_jeu_a_deux_part_1(int(lis[0]), int(lis[1]))                
            elif lis[0] == "nb:":
                if int(lis[1])<self._nb_t:
                    print("veuillez prouver svp!")
            elif len(lis)>2:
                print(lis)
                self._plaques_tirees.clear()
                self._plaques_tirees = [int(i) for i in lis[0:]]
                self._vue.vue_manager.activer_vue_jeu_a_deux_part_2(self._plaques_tirees)
               
    def compte_a_rebours(self, label,  temps, id):
        """
            La méthode compte à rebours
        """
        label.config(text = "%d secondes" %temps)
        if temps > 0:
             self._vue.vue_manager.section_1._id = label.after(1000, lambda:self.compte_a_rebours (label, temps - 1, self._vue.vue_manager.section_1._id ))
        else:
            self._vue.vue_manager.section_1.desactiver_btn_stop()
            self._vue.vue_manager.nombre_trouver()
            self._vue.vue_manager.btn_nb_trouver()
            self._vue.vue_manager.section_1.stop_compte_a_rebours()
            
    def agent_nb_trouver(self, n):
        try:
            self._nb_t = int(n)
            IvySendMsg("nb:,"+ str(self._nb_t))
        except:
            self.lancer_une_alerte("Donnez un nombre SVP !")
    
    def on_connection_change(self, agent, event):
        if len(IvyGetApplicationList()) != 0:
            self._vue.supp_definir_temps()
            self._vue.vue_manager.supprimer_vp()
            
        if event == IvyApplicationDisconnected:
            print(f"L'agent {agent} vient de se deconnecter.")
            
        if event == IvyApplicationConnected:
            try:
                IvySendMsg(str(str(self._temps) +','+ str(self._N)))
                IvySendMsg(str(self.les_plaques_tirees()))
                self._vue.vue_manager.activer_vue_jeu_a_deux_part_1(int(self._temps), self._N)
                self._vue.vue_manager.activer_vue_jeu_a_deux_part_2(self._plaques_tirees)
            finally:
                print(f"mise à jour des agents : {IvyGetApplicationList()}")
            
    def creat_agent(self, name, readMsg=""):
        """
        """
        IvyInit(name, readMsg, 0, self.on_connection_change, self.on_die)
        IvyStart()
        IvyBindMsg(self.get_msg, "(.*)")
  
    def creer_agent_jeu_a_deux(self, pseudo):
        """
        """
        if self.cree_joueur(pseudo) == None:
            self.lancer_une_alerte("Votre nom doit obligatoirement commencé par une lettre !")
        else:
            self.creat_agent(pseudo)     #creation d'agent
            self._vue.cacher_vue_creer_joueur()
            self._vue.definir_temps()
        
    def stop_compte_a_rebours(self):
        """
        """
        #IvySendMsg(str(self.les_plaques_tirees()))
        IvySendMsg("trouver")
        self._vue.vue_manager.section_1.stop_compte_a_rebours()
        self._vue.vue_manager.section_1.desactiver_btn_stop()
    
    def annuller_operation(self):
        """
        """
        self._vue.vue_manager.section_2.annuller_derniere_operation()
        self._vue.vue_manager.desactiver_bouton_effectuer()
        
        self._indices.clear()
        self._operandes.clear()
        self._op_select = False

    def retourner_accueil(self):
        self._vue.supprimer_vue_manager()
        #On crée la vue accueil
        self._vue.activer_vue_accueil()
  
    def lancer_la_vue(self):
        """
            Lance la vue
        """
        self._vue.mainloop()