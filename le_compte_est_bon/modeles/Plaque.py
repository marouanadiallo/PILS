#encoding:utf-8
import random as rd
class Plaque:
    """
        Cette classe définie une liste des plaques et une méthode tirage 
    """
    
    liste_plaques = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,25,25,50,50,75,75,100,100]
    
    @classmethod
    def tirage(self, n):
        """
            Cette méthode restitue une liste contenant 6 chiffres appellé plaque
        """
        return rd.sample(Plaque.liste_plaques, n)
       
        