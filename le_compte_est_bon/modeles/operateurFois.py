#encoding:utf-8

class OperateurFois:
    """
    """
    
    def __init__(self, suivant):
        self._suivant = suivant
        
    def effectuer(self, operande_1, operande_2, index_operateur):
        if index_operateur == 2:
            return operande_1 * operande_2
        else:
            return self._suivant.effectuer(operande_1, operande_2, index_operateur)