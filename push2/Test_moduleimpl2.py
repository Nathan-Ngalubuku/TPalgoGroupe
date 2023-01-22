#TP ALGORITHMIQUE ET INFORMATIQUE
""" 
TRAVAIL FAIT PAR LES MEMBRES DU GROUPE A SAVOIR : NGALUBUKU, RUKENGEZA, SHUKANYA 

"""

import unittest
from math import *
from module_impl2 import *


class TestGeometricform(unittest.TestCase):
    def test_rectangle(self):     # Pour tester le perimetre et la surface du rectangle
        rectangle = Rectangle(5,6)
        self.assertEqual(rectangle.perimeter(), 22)
        self.assertEqual(rectangle.surface(), 30)

    def test_circle(self):      #Pour tester le perimetre et la surface du cercle
        circle = Circle(7)
        self.assertEqual(circle.perimeter(), 2*pi*7)
        self.assertEqual(circle.surface(), pi*7**2)

    def test_triangle(self):        #Pour tester le perimetre et la surface d'un triangle quelconque
        triangle = Triangle(3,4,5,6)
        self.assertEqual(triangle.perimeter(), 15)
        self.assertEqual(triangle.surface(), 6)

    def test_carre(self):        # Pour tester le perimetre et la surface du carré
        square = Square(5)
        self.assertEqual(square.perimeter(), 20)
        self.assertEqual(square.surface(), 25)

    def test_trirectangle(self):         #Pour tester le perimetre et la surface d'un triangle rectangle
        trectangle = TriangleRectangle(3,4,5)
        self.assertEqual(trectangle.perimeter(), 12)
        self.assertEqual(trectangle.surface(), 6)


if __name__ == '__main__':
    unittest.main()