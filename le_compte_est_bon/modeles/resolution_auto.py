from datas.donnees_vue import LES_OPERATEURS

class Resolution():

    def __init__(self):
        self._nombre_plus_proche = 0
        self._min_difference = 1000
        self._liste_operations = list()

    def resolution_automatique(self, liste_plaques:list, max,  chaine_res):
        """
            
        """
        for op in range(0, 4):
            for plaque_1 in range(1, max):
                for plaque_2 in range(plaque_1 + 1, max + 1):
                    resultat = chaine_res.effectuer(liste_plaques[plaque_1], liste_plaques[plaque_2], op)
                    if resultat != None and resultat > 0:
                        if resultat == liste_plaques[0]:
                            self._liste_operations.append([liste_plaques[plaque_1], LES_OPERATEURS[op], liste_plaques[plaque_2], "=", resultat])
                            trouver = True
                            return trouver
                        else:
                            ecart = resultat - liste_plaques[0]
                            if ecart < 0 :
                                ecart = - ecart
                            elif ecart < self._min_difference :
                                self._min_difference = ecart
                                self._nombre_plus_proche = resultat
                                
                        copie_liste_plaques = liste_plaques[:]
                        copie_liste_plaques[plaque_1] = resultat
                        copie_liste_plaques[plaque_2] = 0
                        
                        while True:
                            echange = False
                            for i in range(1, max):
                                if copie_liste_plaques[i] < copie_liste_plaques[i +1] :
                                    tmp = copie_liste_plaques[i]
                                    copie_liste_plaques[i] = copie_liste_plaques[i +1]
                                    copie_liste_plaques[i +1] = tmp
                                    echange = True
                            if not echange :
                                break
                            trouve = self.resolution_automatique(copie_liste_plaques, max - 1,  chaine_res)
                            if trouve:
                                self._liste_operations.append([liste_plaques[plaque_1], LES_OPERATEURS[op], liste_plaques[plaque_2], "=", resultat])
                                return trouve

