""" TRAVAIL FAIT PAR LES MEMBRES DU GROUPE 17 : NGALUBUKU, RUKENGEZA, SHUKANYA"""

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