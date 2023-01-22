#TP ALGORITHMIQUE ET INFORMATIQUE

""" 
TRAVAIL FAIT PAR LES MEMBRES DU GROUPE A SAVOIR : NGALUBUKU, RUKENGEZA, SHUKANYA 

"""

import unittest
import math
from notreTP import Rectangle, Circle, Triangle, Square, TriangleRectangle

class TestGeometricform(unittest.TestCase):
    def test_rectangle(self):    
        rectangle = Rectangle("Rectangle 01",3,4)
        self.assertEqual(rectangle.perimeter(), 14)
        self.assertEqual(rectangle.surface(), 12)

    def test_cercle(self):
        circle = Circle("Cercle A1",5)
        self.assertEqual(circle.perimeter(), 2*math.pi*5)
        self.assertEqual(circle.surface(), math.pi*5**2)

    def test_triangle(self):
        triangle = Triangle("Triangle T1 ",3,4,5)
        self.assertEqual(triangle.perimeter(), 12)
        self.assertEqual(triangle.surface(), 6)

    def test_square(self):
        square = Square("Carre Cr1 ",6)
        self.assertEqual(square.perimeter(), 24)
        self.assertEqual(square.surface(), 36)

    def test_trectangle(self):
        trectangle = TriangleRectangle("Triangle Rectangle TR1 ",3,4)
        self.assertEqual(trectangle.perimeter(), 12)
        self.assertEqual(trectangle.surface(), 6)
        
if __name__ == '__main__':
    unittest.main()