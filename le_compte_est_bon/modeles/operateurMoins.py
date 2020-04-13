#encoding:utf-8
from modeles.operateurFois import OperateurFois
class OperateurMoins:
    """
    """
    
    def __init__(self, suivant:OperateurFois):
        self._suivant = suivant
    
    
    def effectuer(self, operande_1, operande_2, index_operateur):
        if index_operateur == 1:
            if operande_1 >= operande_2:
                return operande_1 - operande_2
            else:
                return operande_2 - operande_1
        else:
            return self._suivant.effectuer(operande_1, operande_2, index_operateur)