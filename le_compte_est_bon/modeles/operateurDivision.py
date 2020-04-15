#encoding:utf-8

class OperateurDivision:
    """
    """
    
    def __init__(self, suivant):
        self._suivant = suivant
    
    
    def effectuer(self, operande_1, operande_2, index_operateur):
        if index_operateur == 3:
            if operande_1 % operande_2 == 0:
                return operande_1 // operande_2
            elif operande_2 % operande_1 == 0:
                return operande_2 // operande_1
            else:
                return None
        else:
            return None