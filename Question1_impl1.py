""" TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 : NGALUBUKU, RUKENGEZA, SHUKANYA """

""" QUESTION NUMERO 1 """

from abc import ABCMeta, abstractmethod
from math import pi, sqrt

class GeomForm(metaclass = ABCMeta): # Creation de la classe de base abstraite
    @abstractmethod
    def perimeter(): # Definition de la fonction perimeter dont le code n'est pas defini, elle devient donc abstraite
        pass

    @abstractmethod
    def surface(): # Definition de la fonction surface dont le code n'est pas defini, elle devient donc abstraite
        pass
    
    def descript(self):
        print("Soit {}\nLe Perimetre est : {}\nLa Surface est : {}".format(self.name, self.perimeter(), self.surface()))