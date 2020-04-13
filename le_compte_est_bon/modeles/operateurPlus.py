#encoding:utf-8
from modeles.operateurMoins import OperateurMoins

class OperateurPlus:
    """
    """
    
    def __init__(self, suivant:OperateurMoins):
        self._suivant = suivant
        
    def effectuer(self, operande_1, operande_2, index_operateur):
        if index_operateur == 0:
            return operande_1 + operande_2
        else:
            return self._suivant.effectuer(operande_1, operande_2, index_operateur)