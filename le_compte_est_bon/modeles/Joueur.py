#encoding:utf-8
from modeles.operateurDivision import OperateurDivision
from modeles.operateurFois import OperateurFois
from modeles.operateurMoins import OperateurMoins
from modeles.operateurPlus import OperateurPlus

class Joueur:
    """
        Cette classe d'écris un joueur
        Un joueur à nom, il a également la liste de toutes les opération qu'il effectuera au cours de son jeu
        il a également un score.
        
        Il effectue les opérations par le biais d'une chaine de responsabilité
    """
    _division, _fois, _moins, _plus =  None, None, None, None
    def __init__(self, nom):
        self._nom = nom
        self._score = 0
        self._liste_operations = list()
    
    
    def effectuer_une_operation(self, operande_1, operande_2, index_operateur):
        """
            Effectue l'opération choisie par le joueur
                Cette opération est faite par le biais de la chaine de responsabilité construite ci-dessous
        """
        
        #construction de la chaine de responsabilité
        Joueur._division = OperateurDivision(None)
        Joueur._fois = OperateurFois(Joueur._division)
        Joueur._moins = OperateurMoins(Joueur._fois)
        Joueur._plus = OperateurPlus(Joueur._moins)
        
        self._resultat = Joueur._plus.effectuer( operande_1, operande_2, index_operateur)
        if self._resultat != None:
            #contruction de l'operation effectuée pour l'historique
            self.ajouter_operation([operande_1, operande_2, self._resultat])
            return self._resultat
        else:
            return None
    
    def ajouter_operation(self, operation):
        """
            Ajoute operation dans la liste des opérations
        """
        self._liste_operations.append(operation)
    
    def supprime_derniere_operation(self):
        """
            Supprime la dernière opération de la liste et restitue l'opération supprimée
        """
        return self._liste_operations.pop()
    def get_derniere_operation(self):
        """
            retourne la dernière opération
        """
        return self._liste_operations[-1]
        
    @property
    def score(self):
        """
            retourne le score
        """
        return self._score
    
    @score.setter
    def score(self, valeur):
        """
            setter de la variable d'instance score
        """
        self._score += valeur
        
        