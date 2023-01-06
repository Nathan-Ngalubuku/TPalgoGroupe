#TP ALGORITHMIQUE ET INFORMATIQUE
"""
TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 A SAVOIR : NGALUBUKU, RUKENGEZA, SHUKANYA

"""
from abc import ABCMeta, abstractmethod
from math import pi, sqrt

""" QUESTION NUMERO 1 """

class GeomForm(metaclass = ABCMeta): # Creation de la classe de base abstraite
    @abstractmethod
    def perimeter(): # Definition de la fonction perimeter dont le code n'est pas defini, elle devient donc abstraite
        pass

    @abstractmethod
    def surface(): # Definition de la fonction surface dont le code n'est pas defini, elle devient donc abstraite
        pass
    
    def descript(self):
        print("Soit {}\nLe Perimetre est : {}\nLa Surface est : {}".format(self.name, self.perimeter(), self.surface()))
        
""" QUESTION NUMERO 2 """

class Rectangle(GeomForm): # Creation de la classe Rectangle heritant de la classe GeomForm
    try:
        def __init__(self,name, length, width):
            self.name = name
            self.length = length
            self.width = width
        def perimeter(self):
            return 2*self.length + 2*self.width
        
        def surface(self):
            return self.length*self.width
    except:
        print("ERREUR SUR LE PARAMETRE INSERER .")

class Circle(GeomForm):  #Creation de la classe Circle heritant de la classe GeomForm
    try:
        def __init__(self, name, radius):
            self.name = name
            self.radius = radius
        def perimeter(self): 
            return 2*pi*self.radius
        def surface(self):
            return  pi*(self.radius**2)
    except:
        print("ERREUR SUR LE PARAMETRE INSERER . ")

class Triangle(GeomForm): # Creation de la classe Triangle heritant de la classe GeomForm
    try:
        def __init__(self,name, c1,c2,c3):
            self.name = name
            self.c2 = c2
            self.c1 = c1
            self.c3 = c3
        def perimeter(self):
            return self.c2 + self.c1 + self.c3

        def surface(self):
            k = self.perimeter()/2
            area = sqrt(k*(k - self.c1)*(k - self.c2)*(k - self.c3))
            area = area.real
            return area
    except:
        print("ERREUR SUR LE PARAMETRE INSERER .")

""" QUESTION NUMERO 3 """

class Square(Rectangle): # Creation de la classe Carre heritant de la classe Rectangle
    try:
        def __init__(self,name, side):
            Rectangle.__init__(self, name, side, side)
    except:
        print(" ERREUR SUR LE PARAMETRE INSERER . ")

class TriangleRectangle(Triangle): # Creation de la classe TriangleRectangle heritant de la classe Triangle
    try:
        def __init__(self,name, base, height):
            hyp = sqrt(base**2+height**2)
            Triangle.__init__(self, name, base, height, hyp)
    except:
        print(" ERREUR SUR LE PARAMETRE INSERER . ")

""" QUESTION NUMERO 4 """

class Geometrie(): # Creation de la classe qui exploite les classes des diffentes formes geo pour fournir le perimetre et la surface de celles-ci
    try:
        def __init__(self):
            self.gGeo_rep = []
        def add(self, fig):
            self.gGeo_rep.append(fig)
        def descript(self):
            for g in self.gGeo_rep:
                print("Soit {}\nLe Perimetre est : {}\nLa Surface est : {}".format(g.name, g.perimeter(), g.surface()))
    except:
        print(" ERREUR SUR LE PARAMETRE INSERER . ")

        